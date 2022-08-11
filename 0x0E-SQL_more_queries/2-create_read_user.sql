-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

-- grant select permission to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
