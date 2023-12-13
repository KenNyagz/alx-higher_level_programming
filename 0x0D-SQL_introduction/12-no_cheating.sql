-- update bob's score from second_table

UPDATE second_table
SET score = 10
WHERE second_table.name = 'Bob';
