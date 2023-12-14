-- creates the database hbtn_0d_usa and the table cities

CREATE TABLE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities(
id INT AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL FOREIGN KEY
name VARCHAR(256) NOT NULL
);
