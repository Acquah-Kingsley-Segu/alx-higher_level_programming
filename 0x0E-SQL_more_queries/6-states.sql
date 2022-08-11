-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- logging into the above database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
