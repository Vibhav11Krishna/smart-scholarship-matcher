import streamlit as st
import pandas as pd
import urllib.parse
import time

st.title("🎓 AI Scholarship Recommendation System")
st.markdown("Enter your complete academic and personal background parameters below to evaluate matched scholarship opportunities.")
st.markdown("---")

model = st.session_state.get('model')
encoders = st.session_state.get('encoders')

if model is None or encoders is None:
    st.error("Critical model artifacts (`scholarship_model.pkl` or `label_encoders.pkl`) could not be loaded from root. Please verify file placement.")
    st.stop()

feature_columns = [
    'Name', 'Education Qualification', 'Gender', 'Community', 'Religion', 
    'Exservice-men', 'Disability', 'Sports', 'Annual-Percentage', 
    'Income', 'India'
]

def get_options(col_name):
    if col_name in encoders:
        return list(encoders[col_name].classes_)
    return []

col_left, col_right = st.columns([1.3, 1], gap="large")

with col_left:
    st.subheader("📋 Student Profile Parameters")
    
    # Styled container wrapper for the form inputs
    with st.form("prediction_form"):
        
        # Row 1: Education & Gender
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            education = st.selectbox("Education Qualification", get_options('Education Qualification'))
        with f_col2:
            gender = st.selectbox("Gender", get_options('Gender'))
            
        # Row 2: Community & Religion
        f_col3, f_col4 = st.columns(2)
        with f_col3:
            community = st.selectbox("Community", get_options('Community'))
        with f_col4:
            religion = st.selectbox("Religion", get_options('Religion'))
            
        # Row 3: Income & Academic Percentage Tier
        f_col5, f_col6 = st.columns(2)
        with f_col5:
            income = st.selectbox("Annual Family Income", get_options('Income'))
        with f_col6:
            percentage = st.selectbox("Academic Grade Tier", get_options('Annual-Percentage'))
            
        # Row 4: Special Statuses (Ex-servicemen & Disability)
        f_col7, f_col8 = st.columns(2)
        with f_col7:
            ex_service = st.selectbox("Ex-servicemen Status", get_options('Exservice-men'))
        with f_col8:
            disability = st.selectbox("Disability Status", get_options('Disability'))
            
        # Row 5: Sports Quota & Residency
        f_col9, f_col10 = st.columns(2)
        with f_col9:
            sports = st.selectbox("Sports Quota / Active", get_options('Sports'))
        with f_col10:
            india_status = st.selectbox("Residency Status", get_options('India'))
            
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Evaluate Eligibility 🚀", use_container_width=True)

with col_right:
    st.subheader("🎯 Evaluation Results")
    
    if submitted:
        student_input = {
            'Education Qualification': education, 'Gender': gender, 'Community': community,
            'Religion': religion, 'Exservice-men': ex_service, 'Disability': disability,
            'Sports': sports, 'Annual-Percentage': percentage, 'Income': income, 'India': india_status
        }
        
        all_schemes = encoders['Name'].classes_
        total_schemes = len(all_schemes)
        eligible_schemes = []
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        status_box = st.status("Initializing AI Prediction Pipeline...", expanded=True)
        
        with status_box:
            st.write("🔍 Loading encoder matrices and rule boundaries...")
            time.sleep(0.2)
            st.write(f"⚙️ Scanning {total_schemes} active scholarship criteria rulesets...")
            
            for idx, scheme in enumerate(all_schemes, 1):
                test_row = student_input.copy()
                test_row['Name'] = scheme
                
                encoded_vals = []
                for col in feature_columns:
                    val = str(test_row[col])
                    if val in encoders[col].classes_:
                        encoded_vals.append(encoders[col].transform([val])[0])
                    else:
                        encoded_vals.append(0)
                        
                X_sample = pd.DataFrame([encoded_vals], columns=[f'{col}_encoded' for col in feature_columns])
                prediction = model.predict(X_sample)[0]
                decoded_outcome = encoders['Outcome'].inverse_transform([prediction])[0]
                
                if str(decoded_outcome) == '1':
                    eligible_schemes.append(scheme)
                
                current_progress = idx / total_schemes
                progress_bar.progress(current_progress)
                progress_text.text(f"Evaluating scheme {idx} of {total_schemes}: {scheme[:30]}...")
            
            status_box.update(label="✅ Evaluation Complete!", state="complete", expanded=False)
        
        progress_bar.empty()
        progress_text.empty()
        
        if eligible_schemes:
            st.success(f"Found **{len(eligible_schemes)}** matching eligible scholarship schemes!")
            
            for idx, scheme in enumerate(eligible_schemes, 1):
                query_url = f"https://www.google.com/search?q={urllib.parse.quote(scheme + ' official portal scholarship')}"
                st.markdown(f"""
                    <div style="background:#ffffff; border:1px solid #e2e8f0; padding:14px; border-radius:10px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:600; color:#0f172a;"><b>{idx}.</b> {scheme}</span>
                        <a href="{query_url}" target="_blank" style="background:#f1f5f9; color:#2563eb; padding:5px 10px; border-radius:6px; text-decoration:none; font-size:13px; border:1px solid #cbd5e1;">🔍 Portal</a>
                    </div>
                """, unsafe_allow_html=True)
            
            results_df = pd.DataFrame({"Matched Scholarship Scheme": eligible_schemes})
            st.download_button(
                label="📥 Download Results (CSV)",
                data=results_df.to_csv(index=False).encode('utf-8'),
                file_name="eligible_scholarships.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.warning("No eligible scholarships found matching this exact profile criteria configuration.")
    else:
        st.info("👈 Fill out your profile configurations on the left panel and click **Evaluate Eligibility**.")