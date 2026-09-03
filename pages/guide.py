import streamlit as st

st.title("📖 User Guide & Documentation")
st.markdown("Step-by-step instructions on how to navigate and utilize the Scholarship Intelligence Platform effectively.")
st.markdown("---")

st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px; margin-bottom:20px;">
        <h3>🚀 Getting Started</h3>
        <p style="color: #475569; line-height: 1.6;">
            The platform is designed to instantly evaluate student profiles against extensive rule matrices derived from combined scholarship datasets. 
            Follow the steps below to run your eligibility analysis.
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px;">
            <h3>📋 Step 1: Provide Profile Details</h3>
            <ul style="color: #475569; line-height: 1.8;">
                <li>Navigate to the <b>Prediction Engine</b> page from the sidebar.</li>
                <li>Select your correct education tier, community, religion, and family income bracket.</li>
                <li>Specify any applicable attributes like disability, sports quota, or ex-servicemen status.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px;">
            <h3>🎯 Step 2: Review Results & Portals</h3>
            <ul style="color: #475569; line-height: 1.8;">
                <li>Click <b>Evaluate Eligibility</b> to execute automated rule checks.</li>
                <li>View the list of matching scholarship schemes you qualify for.</li>
                <li>Click the <b>🔍 Portal</b> button next to any scheme to visit its official application webpage.</li>
                <li>Download your matching results as a CSV file using the export button.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; padding:25px; border-radius:12px; margin-top:20px;">
        <h3>📊 Step 3: Explore Analytics</h3>
        <p style="color: #475569; line-height: 1.6;">
            Switch to the <b>Analytics Dashboard</b> page using the sidebar to inspect dataset distributions across education tiers, income brackets, 
            community categories, and overall eligibility ratios.
        </p>
    </div>
""", unsafe_allow_html=True)