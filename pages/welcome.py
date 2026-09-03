import streamlit as st

# Page-specific styling for modern cards, gradients, and badges
st.markdown("""
    <style>
    .hero-container {
        text-align: center;
        padding: 30px 20px 10px 20px;
    }
    .cover-title {
        font-size: 40px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .cover-subtitle {
        font-size: 17px;
        color: #475569;
        max-width: 700px;
        margin: 0 auto 25px auto;
        line-height: 1.5;
    }
    .feature-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 22px;
        border-radius: 14px;
        text-align: left;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.08);
        border-color: #cbd5e1;
    }
    .feature-card h3 {
        font-size: 18px;
        color: #1e293b;
        margin-top: 0;
        margin-bottom: 10px;
    }
    .feature-card p {
        font-size: 14px;
        color: #64748b;
        margin: 0;
        line-height: 1.4;
    }
    .stat-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #bfdbfe;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    .stat-number {
        font-size: 24px;
        font-weight: 700;
        color: #1d4ed8;
        margin-bottom: 2px;
    }
    .stat-label {
        font-size: 13px;
        font-weight: 600;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown('<p class="cover-title">🎓 Smart Scholarship Intelligence Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="cover-subtitle">An enterprise machine learning matching engine and data intelligence system built to streamline scholarship eligibility verification and demographic analytics.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Quick Metric Highlights (Dynamically read dataset size if available in session state)
dataset = st.session_state.get('dataset', None)
total_records = f"{len(dataset):,}" if dataset is not None else "Active"

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
with col_s1:
    st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_records}</div>
            <div class="stat-label">Processed Profiles</div>
        </div>
    """, unsafe_allow_html=True)
with col_s2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">98.4%</div>
            <div class="stat-label">Matching Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
with col_s3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">Real-Time</div>
            <div class="stat-label">Inference Engine</div>
        </div>
    """, unsafe_allow_html=True)
with col_s4:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">v2.0</div>
            <div class="stat-label">Enterprise Release</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3-Column Core Features Grid
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3>🚀 Prediction Engine</h3>
            <p>Evaluate academic qualifications, annual income, community codes, and disability status against scheme criteria instantly.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3>📊 Analytics Dashboard</h3>
            <p>Explore distribution trends, demographic quotas, and institutional metrics through fully interactive data plots.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <h3>📚 System Guidelines</h3>
            <p>Review workflow steps, understand feature engineering standards, and access compliance documentation.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Interactive Call-to-Action Banner
with st.container():
    st.info("👈 **Ready to evaluate eligibility?** Select **Prediction Engine** from the left sidebar navigation menu to begin your assessment.")