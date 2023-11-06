-- creacion tabla usuarios
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  hashed_password VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- creacion tabla logs
CREATE TABLE logs (
  log_id SERIAL PRIMARY KEY,
  evento VARCHAR(50) NOT NULL,
  user_email VARCHAR(100) NOT NULL,
  fecha_log TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_email) REFERENCES users(email)
);

-- Insertar datos de prueba en la tabla users
INSERT INTO users (username, hashed_password, email) VALUES
  ('Cristiano Ronaldo', '11', 'cristiano_r@email.com'),
  ('Pepito perez', '12', 'pepito_p@email.com'),
  ('Ricardo Jorge', '13', 'ricardo_j@email.com'),
  ('Adolf Hitler', '14', 'adolf_h@email.com'),
  ('Rocket Raccoon', '15', 'rocket_r@email.com'),
  ('Isaac Newton', '16', 'isaac_n@email.com');
  ('Lila Mikel', '17', 'lila_m@email.com');

