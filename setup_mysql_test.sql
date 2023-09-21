-- Creates the hbnb_test_db database if database does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates in localhost with hbnb_test_pwd password, hbnb_test user 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the database hbnb_test_db to hbnb_test 
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege (for database performance_schema) to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';