-- this SQL script selects the score and name from the second_table, filtering for scores greater than or equal to 10, and ordering the results by score in descending order.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;