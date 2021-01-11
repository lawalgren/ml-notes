SELECT age, COUNT(age) AS occurances 
FROM <AWS_GLUE_TABLE_NAME>
GROUP BY age
ORDER BY occurances DESC
LIMIT 5;