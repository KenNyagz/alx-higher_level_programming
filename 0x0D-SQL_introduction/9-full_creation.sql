-- create a second table in a db and add multiple rows

CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` VALUES ('1', 'JOHN', '10'), ('2', 'ALEX', '3'), ('3', 'BOB', '14'), ('4', 'GEORGE', '8');
