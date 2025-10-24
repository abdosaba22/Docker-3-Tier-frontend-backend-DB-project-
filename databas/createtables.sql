USE db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    major VARCHAR(100)
);

INSERT INTO students (name, major) VALUES ('Abdalrahman Amin', 'ITI');
INSERT INTO students (name, major) VALUES ('Ibrahim Amin', 'PT');
