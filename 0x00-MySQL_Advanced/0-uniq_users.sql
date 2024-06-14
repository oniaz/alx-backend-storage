-- task 0
-- creates a table users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL UNIQUE, 
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
