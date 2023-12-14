--  lists all the cities of California that can be found in the database hbtn_0d_usa

USE hbtn_0d_usa;
SELECT id FROM states WHERE name = 'California' AS cali_id;
SELECT name FROM cities WHERE state_id = cali_id;
-- ORDER BY cities.id ASC;
