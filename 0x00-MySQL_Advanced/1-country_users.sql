-- This script creates a table users
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(225) NOT NULL UNIQUE,
	name VARCHAR(225),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
