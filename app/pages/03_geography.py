import streamlit as st
import plotly.express as px
import duckdb

st.title("🌍 Geographic Distribution")
st.markdown("Where are the most job opportunities?")

@st.cache_data
def load_data():
    conn = duckdb.connect()
    conn.execute("CREATE VIEW jobs AS SELECT * FROM 'data/processed/jobs.parquet'")
    df = conn.execute("""
        SELECT location,
               COUNT(DISTINCT job_id) AS job_count,
               ROUND(AVG(normalized_salary)) AS avg_salary
        FROM jobs
        WHERE location IS NOT NULL
        AND location NOT IN ('United States', 'New York, United States', 'California, United States')
        GROUP BY location
        ORDER BY job_count DESC
        LIMIT 20
    """).df()
    return df

df = load_data()

fig = px.bar(
    df,
    x='job_count',
    y='location',
    color='avg_salary',
    orientation='h',
    title='Top 20 Cities by Job Count',
    labels={'job_count': 'Number of Jobs', 'location': 'Location', 'avg_salary': 'Avg Salary'}
)

fig.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=550
)

st.plotly_chart(fig, use_container_width=True)

st.info("💡 New York leads in volume. San Francisco Bay Area leads in salary at $160K average.")