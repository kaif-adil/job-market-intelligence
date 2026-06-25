import streamlit as st
import plotly.express as px
import duckdb

st.title("🔧 Skill Demand")
st.markdown("Which skills appear most frequently in job postings?")

@st.cache_data
def load_data():
    conn = duckdb.connect()
    conn.execute("CREATE VIEW skills AS SELECT * FROM 'data/processed/skills.parquet'")
    df = conn.execute("""
        SELECT skill_name, skill_category, COUNT(DISTINCT job_id) AS job_count
        FROM skills
        GROUP BY skill_name, skill_category
        ORDER BY job_count DESC
        LIMIT 25
    """).df()
    return df

df = load_data()

categories = ['All'] + sorted(df['skill_category'].unique().tolist())
selected_category = st.selectbox('Filter by skill category:', categories)

if selected_category != 'All':
    df = df[df['skill_category'] == selected_category]


fig = px.bar(
    df,
    x='job_count',
    y='skill_name',
    color='skill_category',
    orientation='h',
    title='Top 25 Most Demanded Skills',
    labels={'job_count': 'Number of Jobs', 'skill_name': 'Skill'}
)

fig.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=550
)

st.plotly_chart(fig, use_container_width=True)

st.info("💡 Excel dominates at 18,107 jobs — driven by business analyst and operations roles. Python and SQL lead among technical data roles.")