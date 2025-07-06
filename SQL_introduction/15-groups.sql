-- this SQL script counts the number of records in the second_table grouped by score, ordering the results by the count in descending order.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;