SELECT 
    a.skill_name AS skill_a,
    b.skill_name AS skill_b,
    COUNT(DISTINCT a.job_id) AS co_count
FROM 'data/processed/skills.parquet' AS a
JOIN 'data/processed/skills.parquet' AS b
    ON a.job_id = b.job_id
    AND a.skill_name < b.skill_name 
GROUP BY skill_a, skill_b
HAVING co_count > 50
ORDER BY co_count DESC
LIMIT 20;