import streamlit as st
import plotly.express as px
import duckdb

st.title("💰 Salary Analysis")
st.markdown("Which skills command the highest salaries?")

@st.cache_data
def load_data():
    conn = duckdb.connect()
    conn.execute("CREATE VIEW jobs AS SELECT * FROM 'data/processed/jobs.parquet'")
    conn.execute("CREATE VIEW skills AS SELECT * FROM 'data/processed/skills.parquet'")
    df = conn.execute("""
        SELECT s.skill_name, s.skill_category,
               ROUND(AVG(j.normalized_salary)) AS avg_salary,
               COUNT(DISTINCT j.job_id) AS job_count
        FROM jobs j
        JOIN skills s ON j.job_id = s.job_id
        WHERE j.normalized_salary IS NOT NULL
        GROUP BY s.skill_name, s.skill_category
        HAVING COUNT(DISTINCT j.job_id) > 100
        ORDER BY avg_salary DESC
    """).df()
    return df

df = load_data()

fig = px.bar(
    df,
    x='avg_salary',
    y='skill_name',
    color='skill_category',
    orientation='h',
    title='Average Salary by Skill',
    labels={'avg_salary': 'Average Salary (USD)', 'skill_name': 'Skill'}
)

fig.update_layout(yaxis={'categoryorder': 'total ascending'},height=550)

st.plotly_chart(fig, use_container_width=True)

st.info("💡 Deep Learning and ML skills pay 25-40% above the average. Excel pays the least despite being the most demanded skill.")

st.markdown("---")
st.subheader("💡 Salary vs Demand — The Full Picture")
st.markdown("Each bubble is one skill. Size = how many jobs require it.")

fig2 = px.scatter(
    df,
    x='job_count',
    y='avg_salary',
    size='job_count',
    color='skill_category',
    text='skill_name',
    title='Skill Value Map — Demand vs Salary',
    labels={
        'job_count': 'Number of Jobs (Demand)',
        'avg_salary': 'Average Salary (USD)'
    },
    size_max=60
)

fig2.update_traces(textposition='top center', textfont_size=10)
fig2.update_layout(height=600)

st.plotly_chart(fig2, use_container_width=True)

st.info("💡 Top right = high demand AND high salary (Python, AWS) — the sweet spot. Top left = niche premium skills (Deep Learning). Bottom right = commoditized skills (Excel) — high demand but lower pay.")