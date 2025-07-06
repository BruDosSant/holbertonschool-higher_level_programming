-- this SQL script selects the score and name from the second_table, filtering for non-null and non-empty names, and ordering the results by score in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;