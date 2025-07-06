-- a script to select the id and name of cities in California, ordered by id in ascending order
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;