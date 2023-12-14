--  lists all cities contained in the database hbtn_0d_usa

USE hbtn_0d_usa;

SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM hbtn_0d_usa.cities
JOIN htbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC;
