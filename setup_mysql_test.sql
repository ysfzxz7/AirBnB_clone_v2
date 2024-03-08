-- these mysql commands creates new database if not exists,
-- and new user if not exists and grants him all privileges
-- to the created database, and flush the changes.

-- create database named 'hbnb_test_db' if not exists.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user named 'hbnb_test' at 'localhost' if not exists.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant 'hbnb_test' all privileges on 'hbnb_test_db'.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- flush privileges.
FLUSH PRIVILEGES;
-- grant SELECT privileges on 'performance_schema' database to user 'hbnb_test'.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges.
FLUSH PRIVILEGES;
