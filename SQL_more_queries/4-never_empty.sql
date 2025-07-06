-- a script to create a table named id_not_null with two columns: id and name
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);