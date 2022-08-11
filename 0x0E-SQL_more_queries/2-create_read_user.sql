-- create a database
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;

-- create a user
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

-- grant select permission to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
