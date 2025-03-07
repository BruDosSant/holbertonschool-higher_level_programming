-- Obtener el id de California
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- Listar las ciudades de California, ordenadas por cities.id
SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;
