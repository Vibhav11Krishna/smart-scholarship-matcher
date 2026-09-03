import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Scholarship Intelligence Dashboard")
st.markdown("Real-time telemetry, dataset distribution insights, and advanced eligibility mapping analytics.")
st.markdown("---")

df = st.session_state.get('dataset')

if df is None:
    st.error("Dataset `dataset_combined.xlsx` not found in root directory.")
    st.stop()

# Key Metric Computations
total_rows = len(df)
total_schemes = df['Name'].nunique() if 'Name' in df.columns else 0
eligible_count = len(df[df['Outcome'] == 1]) if 'Outcome' in df.columns else 0
eligibility_rate = (eligible_count / total_rows) * 100 if total_rows > 0 else 0

# Metric Cards Row
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Total Records", f"{total_rows:,}")
with m2:
    st.metric("Unique Schemes", f"{total_schemes:,}")
with m3:
    st.metric("Eligible Matches", f"{eligible_count:,}")
with m4:
    st.metric("Eligibility Ratio", f"{eligibility_rate:.2f}%")

st.markdown("<br>", unsafe_allow_html=True)

# Row 1 Charts: Education Tier & Family Income
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🎓 Schemes by Education Tier")
    if 'Education Qualification' in df.columns:
        edu_counts = df['Education Qualification'].value_counts().reset_index()
        edu_counts.columns = ['Qualification', 'Count']
        chart_edu = alt.Chart(edu_counts).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color="#2563eb").encode(
            x=alt.X('Qualification:N', sort='-y', title='Education Tier', axis=alt.Axis(labelAngle=-20)),
            y=alt.Y('Count:Q', title='Record Volume'),
            tooltip=['Qualification', 'Count']
        ).properties(height=320).configure_view(stroke=None)
        st.altair_chart(chart_edu, use_container_width=True)

with col_right:
    st.subheader("💰 Family Income Tier Distribution")
    if 'Income' in df.columns:
        income_counts = df['Income'].value_counts().reset_index()
        income_counts.columns = ['Income Bracket', 'Count']
        chart_income = alt.Chart(income_counts).mark_arc(innerRadius=70, padAngle=0.04).encode(
            theta=alt.Theta('Count:Q'),
            color=alt.Color('Income Bracket:N', legend=alt.Legend(title="Income Tier", orient="right")),
            tooltip=['Income Bracket', 'Count']
        ).properties(height=320).configure_view(stroke=None)
        st.altair_chart(chart_income, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 2 Charts: Community Breakdown & Gender Distribution
col_c1, col_c2 = st.columns(2, gap="large")

with col_c1:
    st.subheader("🏛️ Community Demographics Distribution")
    if 'Community' in df.columns:
        comm_counts = df['Community'].value_counts().reset_index()
        comm_counts.columns = ['Community', 'Count']
        chart_comm = alt.Chart(comm_counts).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color="#10b981").encode(
            x=alt.X('Community:N', sort='-y', title='Community Category', axis=alt.Axis(labelAngle=-15)),
            y=alt.Y('Count:Q', title='Volume'),
            tooltip=['Community', 'Count']
        ).properties(height=320).configure_view(stroke=None)
        st.altair_chart(chart_comm, use_container_width=True)

with col_c2:
    st.subheader("🚻 Gender Quota Breakdown")
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        chart_gender = alt.Chart(gender_counts).mark_arc(innerRadius=50, outerRadius=100, padAngle=0.06).encode(
            theta=alt.Theta('Count:Q'),
            color=alt.Color('Gender:N', legend=alt.Legend(title="Gender Group", orient="right")),
            tooltip=['Gender', 'Count']
        ).properties(height=320).configure_view(stroke=None)
        st.altair_chart(chart_gender, use_container_width=True)

st.markdown("---")

# Interactive Raw Data Explorer Section
st.subheader("🔍 Dataset Telemetry Inspector")
st.markdown("Search or filter through the underlying active scholarship records loaded in memory.")

search_query = st.text_input("Filter by Scholarship Name or Keyword:", "")
if search_query:
    filtered_df = df[df['Name'].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df

st.dataframe(filtered_df.head(100), use_container_width=True)
st.caption(f"Showing preview of {len(filtered_df):,} total matching data rows.")