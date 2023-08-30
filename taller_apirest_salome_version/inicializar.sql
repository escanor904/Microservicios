-- create_users_table.sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  hashed_password VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de prueba en la tabla users
INSERT INTO users (username, hashed_password, email) VALUES
  ('Pepito perez', '12', 'pepito_p@email.com'),
  ('Ricardo Jorge', '13', 'ricardo_j@email.com'),
  ('Adolf Hitler ', '14', 'adolf_h@email.com'),
  ('Cristiano Ronaldo', '15', 'cristiano_r@email.com'),
  ('Rocket Raccoon', '16', 'rocket_r@email.com');
  ('Isaac Newton', '16', 'isaac_n@email.com');

