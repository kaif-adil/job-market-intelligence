import streamlit as st
import plotly.express as px
import duckdb

st.title("🔗 Skill Combinations")
st.markdown("Which skills appear together most often in job postings?")

@st.cache_data
def load_data():
    conn = duckdb.connect()
    conn.execute("CREATE VIEW skills AS SELECT * FROM 'data/processed/skills.parquet'")
    df = conn.execute("""
        SELECT 
            a.skill_name AS skill_a,
            b.skill_name AS skill_b,
            COUNT(DISTINCT a.job_id) AS co_count
        FROM skills a
        JOIN skills b
            ON a.job_id = b.job_id
            AND a.skill_name < b.skill_name
        GROUP BY skill_a, skill_b
        HAVING co_count > 50
        ORDER BY co_count DESC
        LIMIT 20
    """).df()
    df['skill_pair'] = df['skill_a'] + ' + ' + df['skill_b']
    return df

df = load_data()

fig = px.bar(
    df,
    x='co_count',
    y='skill_pair',
    orientation='h',
    title='Top 20 Skill Combinations',
    labels={'co_count': 'Jobs Requiring Both Skills', 'skill_pair': 'Skill Pair'},
    color='co_count',
    color_continuous_scale='Blues'
)

fig.update_layout(yaxis={'categoryorder': 'total ascending'},height=550)

st.plotly_chart(fig, use_container_width=True)

st.info("💡 Python + SQL is the most common combination appearing in 1,978 jobs. Docker + Kubernetes almost always appear together.")