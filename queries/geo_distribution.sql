SELECT location, COUNT(DISTINCT job_id) AS job_count, AVG(normalized_salary) AS avg_salary
FROM 'data/processed/jobs.parquet'
WHERE location IS NOT NULL AND normalized_salary IS NOT NULL
GROUP BY location
ORDER BY job_count DESC
LIMIT 30;