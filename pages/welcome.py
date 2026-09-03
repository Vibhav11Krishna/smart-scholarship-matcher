import streamlit as st

st.markdown("""
    <style>
    .cover-container {
        text-align: center;
        padding: 40px 20px;
    }
    .cover-title {
        font-size: 42px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 10px;
    }
    .cover-subtitle {
        font-size: 18px;
        color: #475569;
        margin-bottom: 30px;
    }
    .feature-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        text-align: left;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="cover-container">', unsafe_allow_html=True)
st.markdown('<p class="cover-title">🎓 Smart Scholarship Intelligence Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="cover-subtitle">Advanced machine learning matching engine & telemetry analytics for scholarship schemes.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3>🚀 Prediction Engine</h3>
            <p>Evaluate personal academic, income, and community parameters against active scheme constraints in real time.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3>📊 Analytics Dashboard</h3>
            <p>Explore distribution metrics, demographic quotas, and dataset insights through interactive data visualizations.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <h3>📚 User Guide</h3>
            <p>Learn how to navigate system workflows, interpret eligibility status codes, and access official application portals.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Call-to-action button or navigation reminder
st.info("👈 Select a section from the sidebar navigation menu to get started.")
st.markdown('</div>', unsafe_allow_html=True)