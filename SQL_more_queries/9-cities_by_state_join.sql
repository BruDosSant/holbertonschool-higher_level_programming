-- Listar todas las ciudades con su nombre y el nombre del estado
SELECT 
    cities.id, 
    cities.name, 
    (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
