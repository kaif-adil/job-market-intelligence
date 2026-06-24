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