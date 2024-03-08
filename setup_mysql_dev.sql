-- creates new user and new database.
-- grants all privileges for user on the database created.
-- save the privileges.

-- create hbnb_dev_db database if not exists.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create hbnb_dev at localhost if not exists and set its password to hbnb_dev_pwd.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant the user all privileges on hbnb_dev_db database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- save the privileges.
FLUSH PRIVILEGES;
-- grant SELECT privileges on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- save the privileges.
FLUSH PRIVILEGES;
