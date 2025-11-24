-- Create database and user
CREATE DATABASE IF NOT EXISTS brent_db;
CREATE USER IF NOT EXISTS 'brent_user'@'%' IDENTIFIED BY 'brent_password';
GRANT ALL PRIVILEGES ON brent_db.* TO 'brent_user'@'%';
FLUSH PRIVILEGES;

USE brent_db;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL DEFAULT 'Brent Verlinden',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial data
INSERT IGNORE INTO users (id, name) VALUES (1, 'Brent Verlinden');