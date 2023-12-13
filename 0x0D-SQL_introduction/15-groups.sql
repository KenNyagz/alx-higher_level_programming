-- list the number of records with the same score

SELECT score, COUNT(*) AS record_count
FROM second_table
GROUP BY score
ORDER BY record_count DESC;
