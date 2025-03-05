-- Pablito clvo un clavito cuantos pi****s se comio pablito
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
