-- INSERT 
-- UPDATE
-- DELETE
-- SELECT

-- INSERT INTO table_name ( column_name, column_name)
-- VALUES ( value, value);

INSERT INTO users (name)
VALUES ('Spencer'), ('Bob'),('Alex');

INSERT INTO licenses (number, state, expiration, user_id)
VALUES (4423423,'OR','2022-10-10',1);

INSERT INTO dealerships_have_cars (dealerships_id, cars_id)
VALUES (1,1);

-- SELECT the command to retrieve data from the db
-- SELECT (what to grab) FROM (table to grab from)

SELECT * FROM cars;
SELECT * FROM users;
SELECT name as user_name FROM users WHERE id > 2 ORDER BY name DESC;
SELECT * FROM licenses;
-- UPDATE
-- UPDATE table_name SET column_name = value, column_name = value
-- WHERE condition
UPDATE users SET name = 'Melissa';
UPDATE licenses SET number = '123435', state = 'WA' WHERE id = 1;

-- DELETE
-- DELETE FROM table_name WHERE condition;

DELETE FROM users WHERE id = 2;
SELECT *, HOUR(updated_at) as hour_updated FROM cars;
-- 
SELECT *, COUNT(id) FROM users GROUP BY name;
-- JOIN table_to_add ON fk = pk;
SELECT * FROM licenses JOIN users ON users.id = licenses.user_id;
-- left join will display the unmatching data from the left side

SELECT * FROM dealerships JOIN dealerships_have_cars ON dealerships.id = dealerships_id JOIN cars ON cars_id = cars.id;