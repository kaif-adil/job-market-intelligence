SELECT skill_name,skill_category,COUNT(DISTINCT job_id) AS job_count FROM 'data/processed/skills.parquet'
GROUP BY skill_name,skill_category
ORDER BY job_count DESC
LIMIT 25;

