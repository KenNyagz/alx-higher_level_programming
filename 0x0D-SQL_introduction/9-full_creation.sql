-- create a second table in a db and add multiple rows

CREATE IF NOT EXISTS `second_table`(`id` INT, `name` VARCHAR(256), `score` INT);
VALUES(1,'JOHN', 10), (2, 'ALEX', 3), (3, 'BOB', 14), (4, 'GEORGE', 8);
