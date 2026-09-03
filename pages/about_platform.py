import streamlit as st

st.title("ℹ️ About Scholarship Intelligence Platform")
st.markdown("An advanced data-driven system built to streamline financial aid discovery, automate eligibility mapping, and provide telemetry analytics.")
st.markdown("---")

st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px; margin-bottom:20px;">
        <h3>🎯 Mission & Purpose</h3>
        <p style="color: #475569; line-height: 1.6;">
            Navigating financial aid is frequently hindered by fragmented data sources, ambiguous eligibility rules, and administrative overhead. 
            The <b>Scholarship Intelligence Platform</b> bridges this gap by centralizing scheme intelligence, applying automated predictive rule-mapping models, 
            and giving students instant clarity on their financial aid prospects.
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px;">
            <h3>🔍 Key Capabilities</h3>
            <ul style="color: #475569; line-height: 1.8;">
                <li><b>Smart Eligibility Mapping:</b> Instantly evaluates criteria across multiple vectors.</li>
                <li><b>Analytics Suite:</b> Comprehensive telemetry tracking distribution metrics.</li>
                <li><b>Dataset Verification:</b> High-performance parsing of large institutional corpora.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px;">
            <h3>⚙️ Technology Stack</h3>
            <p style="color: #475569; margin-bottom: 12px;">Engineered using a modern Python stack:</p>
            <div>
                <span style="background:#f1f5f9; color:#2563eb; padding:5px 10px; border-radius:6px; font-weight:600; font-size:12px; border:1px solid #cbd5e1; display:inline-block; margin:3px;">Streamlit</span>
                <span style="background:#f1f5f9; color:#2563eb; padding:5px 10px; border-radius:6px; font-weight:600; font-size:12px; border:1px solid #cbd5e1; display:inline-block; margin:3px;">Pandas</span>
                <span style="background:#f1f5f9; color:#2563eb; padding:5px 10px; border-radius:6px; font-weight:600; font-size:12px; border:1px solid #cbd5e1; display:inline-block; margin:3px;">Altair</span>
                <span style="background:#f1f5f9; color:#2563eb; padding:5px 10px; border-radius:6px; font-weight:600; font-size:12px; border:1px solid #cbd5e1; display:inline-block; margin:3px;">Scikit-Learn / Joblib</span>
            </div>
        </div>
    """, unsafe_allow_html=True)