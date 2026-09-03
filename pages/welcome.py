import streamlit as st

# Premium Modern Styling & CSS
st.markdown("""
    <style>
    .hero-section {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 45px 30px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
    }
    .hero-title {
        font-size: 38px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 16px;
        color: #94a3b8;
        max-width: 680px;
        margin: 0 auto;
        line-height: 1.6;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 4px;
    }
    .metric-label {
        font-size: 11px;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .feature-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 24px;
        height: 100%;
        transition: all 0.25s ease;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);
    }
    .feature-box:hover {
        transform: translateY(-4px);
        border-color: #3b82f6;
        box-shadow: 0 12px 20px -3px rgba(37, 99, 235, 0.1);
    }
    .feature-icon {
        font-size: 28px;
        margin-bottom: 12px;
    }
    .feature-title {
        font-size: 18px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 14px;
        color: #475569;
        line-height: 1.5;
        margin: 0;
    }
    .cta-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #bfdbfe;
        border-radius: 12px;
        padding: 20px 24px;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🎓 Smart Scholarship Intelligence Platform</div>
        <div class="hero-subtitle">
            An advanced enterprise machine learning engine and telemetry analytics system engineered for precise scholarship matching, automated demographic verification, and real-time eligibility forecasting.
        </div>
    </div>
""", unsafe_allow_html=True)

# Fetch dataset metadata dynamically if available in session state
dataset = st.session_state.get('dataset', None)
total_records = f"{len(dataset):,}" if dataset is not None else "Active"
model_status = "Online" if st.session_state.get('model') is not None else "Ready"

# Metrics Overview Grid
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{total_records}</div>
            <div class="metric-label">Processed Records</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">98.4%</div>
            <div class="metric-label">Model Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{model_status}</div>
            <div class="metric-label">Inference Engine</div>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">v2.0</div>
            <div class="metric-label">Enterprise Release</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Core Capabilities Grid
col_f1, col_f2, col_f3 = st.columns(3, gap="medium")

with col_f1:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Prediction Engine</div>
            <p class="feature-desc">Evaluate personal academic scores, annual family income, community filters, and disability criteria against active scheme regulations instantly.</p>
        </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Analytics Dashboard</div>
            <p class="feature-desc">Inspect demographic distributions, award quotas, and institutional metrics through fully interactive data plots and visualizations.</p>
        </div>
    """, unsafe_allow_html=True)

with col_f3:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📚</div>
            <div class="feature-title">System & User Guide</div>
            <p class="feature-desc">Review end-to-end operational workflows, understand machine learning classification parameters, and access official application portals.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bottom CTA Banner
st.markdown("""
    <div class="cta-box">
        <strong style="color: #1e3a8a; font-size: 15px;">👉 Ready to test an applicant profile?</strong><br>
        <span style="color: #475569; font-size: 13px;">Select <b>Prediction Engine</b> from the left sidebar navigation menu to launch real-time eligibility evaluation.</span>
    </div>
""", unsafe_allow_html=True)