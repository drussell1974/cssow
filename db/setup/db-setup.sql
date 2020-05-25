CREATE USER IF NOT EXISTS 'drussell1974'@'%' IDENTIFIED BY 'password1.';
SELECT User, Host, password_expired FROM mysql.user WHERE User = 'drussell1974';
CREATE DATABASE IF NOT EXISTS cssow_api;
