CREATE TABLE appusers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL
);

-- Insert some sample data
INSERT INTO appusers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');
