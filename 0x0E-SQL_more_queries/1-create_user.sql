-- create a user
CREATE USER IF NOT EXISTS 'usere_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';

-- grant permissions to user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
