CREATE DATABASE vulnerable_db;
CREATE USER 'admin'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON vulnerable_db.* TO 'admin'@'%';
FLUSH PRIVILEGES;
