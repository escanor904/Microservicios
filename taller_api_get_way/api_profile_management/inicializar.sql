-- creacion tabla usuarios
CREATE TABLE profiles (
  email VARCHAR(100) PRIMARY KEY NOT NULL UNIQUE,
  username VARCHAR(50) NOT NULL,
  pagina_personal VARCHAR(300) NOT NULL,
  correspondencia VARCHAR(100) NOT NULL,
  biografia VARCHAR(1000) NOT NULL,
  organizacion VARCHAR(100) NOT NULL,
  pais VARCHAR(100) NOT NULL,
  linkedln_url VARCHAR(300) NOT NULL,
  informacion_publica BOOLEAN NOT NULL
);






-- Insertar datos de prueba en la tabla users
INSERT INTO profiles (email, username, pagina_personal, correspondencia, biografia, organizacion, pais, linkedln_url, informacion_publica)
VALUES
  ('cristiano_r@email.com', 'Cristiano Ronaldo', 'www.ejemplo.com/cristiano', '123 Main St, City', 'Soy un apasionado por el fútbol y los negocios.', 'Real Madrid', 'España', 'https://www.linkedin.com/in/cristianoronaldo', true),
  ('pepito_p@email.com', 'Pepito Perez', 'www.ejemplo.com/pepito', '456 Elm St, City', 'Me gusta el arte y la música.', 'Artistas Unidos', 'México', 'https://www.linkedin.com/in/pepitoperez', true),
  ('ricardo_j@email.com', 'Ricardo Jorge', 'www.ejemplo.com/ricardo', '789 Oak St, City', 'Ingeniero apasionado por la tecnología.', 'Tech Company', 'Brasil', 'https://www.linkedin.com/in/ricardojorge', true),
  ('adolf_h@email.com', 'Adolf Hitler', 'www.ejemplo.com/adolf', '910 Pine St, City', 'Escritor y filósofo.', 'Writer & Co.', 'Alemania', 'https://www.linkedin.com/in/adolfhitler', false),
  ('rocket_r@email.com', 'Rocket Raccoon', 'www.ejemplo.com/rocket', '111 Galaxy St, City', 'Guardián del espacio y amante de los mapaches.', 'Guardians of Galaxy', 'Espacio Exterior', 'https://www.linkedin.com/in/rocketraccoon', true),
  ('isaac_n@email.com', 'Isaac Newton', 'www.ejemplo.com/isaac', '222 Apple St, City', 'Físico y matemático pionero.', 'Royal Society', 'Reino Unido', 'https://www.linkedin.com/in/isaacnewton', true),
  ('lila_m@email.com', 'Lila Mikel', 'www.ejemplo.com/lila', '333 Violet St, City', 'Exploradora del mundo y amante de la naturaleza.', 'Nature Explorers', 'Australia', 'https://www.linkedin.com/in/lilamikel', true);
