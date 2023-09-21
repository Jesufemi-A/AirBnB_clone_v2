-- creates  the hbnb_dev_db database if  database not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create hbnb_dev user in localhost with hbnb_dev_pwd password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on the database hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant SELECT privileges to hbnb_dev 
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';