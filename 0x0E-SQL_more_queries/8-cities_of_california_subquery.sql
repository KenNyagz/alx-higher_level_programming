--  lists all the cities of California that can be found in the database hbtn_0d_usa

USE hbtn_0d_usa;
SELECT id INTO @state_id FROM states WHERE name = 'California';
SELECT name FROM cities WHERE state_id = @state_id;
ORDER BY cities.id ASC;
