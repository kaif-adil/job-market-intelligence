import streamlit as st

st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Job Market Intelligence Platform")
st.markdown("Analyzing 123,842 job postings to uncover skill demand, salary trends, and geographic opportunities.")

st.sidebar.title("Navigation")
st.sidebar.markdown("Select a page above to explore the data.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", "123,842")
with col2:
    st.metric("Skills Tracked", "50+")
with col3:
    st.metric("Jobs With Salary", "35,617")

st.markdown("---")
st.subheader("🔍 What You'll Find Here")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🔧 Skill Demand**")
    st.markdown("Which skills appear most in job postings - filtered by category")
    st.markdown("**💰 Salary Analysis**")
    st.markdown("Which skills pay the most plus a salary vs demand map")

with col2:
    st.markdown("**🌍 Geographic Distribution**")
    st.markdown("Which cities and states have the most opportunities")
    st.markdown("**🔗 Skill Combinations**")
    st.markdown("Which skills always appear together in job postings")

st.markdown("---")
st.caption("Dataset: LinkedIn Job Postings 2023–2024 | Source: Kaggle | Salary analysis based on 35,617 postings that disclosed compensation")