import streamlit as st
import pandas as pd
import joblib

# Global Page Configuration
st.set_page_config(
    page_title="Scholarship Intelligence Platform",
    page_icon="🎓",
    layout="wide"
)

# Global Theme Customization
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        background-color: #2563eb;
        color: white;
        transition: all 0.3s ease;
        border: none;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Cache shared machine learning artifacts globally across pages
@st.cache_resource
def load_shared_artifacts():
    try:
        model = joblib.load('scholarship_model.pkl')
        encoders = joblib.load('label_encoders.pkl')
        return model, encoders
    except Exception:
        return None, None

@st.cache_data
def load_shared_dataset():
    try:
        df = pd.read_excel('dataset_combined.xlsx')
        df.columns = df.columns.str.strip()
        df['Name'] = df['Name'].str.replace(' ? ', ' - ', regex=False).str.replace('?', '-', regex=False)
        return df
    except Exception:
        return None

# Inject into session state for cross-page availability
st.session_state['model'], st.session_state['encoders'] = load_shared_artifacts()
st.session_state['dataset'] = load_shared_dataset()

# Native Streamlit Multi-Page Navigation Setup
pages = [
    st.Page("pages/welcome.py", title="Welcome & Overview", default=True),
    st.Page("pages/home_prediction.py", title="Prediction Engine"),
    st.Page("pages/analytics_dashboard.py", title="Analytics Dashboard"),
    st.Page("pages/about_platform.py", title="About Platform"),
    st.Page("pages/guide.py", title="User Guide")
]

pg = st.navigation(pages, position="sidebar")

# Render system status metadata in the persistent sidebar footer
with st.sidebar:
    st.markdown("---")
    st.markdown("### 📌 System Status")
    if st.session_state['model'] is not None:
        st.success("🟢 Model Active & Healthy")
    else:
      st.error("🔴 Artifacts Missing")
    st.markdown(
        "<div style='text-align: center; color: #64748b; font-size: 12px; margin-top: 15px;'>"
        "Scholarship Intelligence v2.0<br>© 2026 Enterprise Edition"
        "</div>", 
        unsafe_allow_html=True
    )

pg.run()