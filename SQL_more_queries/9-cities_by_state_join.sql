-- a script to select the id, name of cities and the name of their states, ordered by city id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;