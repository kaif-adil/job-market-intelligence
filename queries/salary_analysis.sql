SELECT s.skill_name, s.skill_category,AVG(j.normalized_salary) AS avg_salary
FROM 'data/processed/jobs.parquet' AS j
JOIN 'data/processed/skills.parquet' AS s
ON j.job_id = s.job_id
WHERE j.normalized_salary IS NOT NULL
GROUP BY s.skill_name, s.skill_category
HAVING COUNT(DISTINCT j.job_id) > 100
ORDER BY avg_salary DESC