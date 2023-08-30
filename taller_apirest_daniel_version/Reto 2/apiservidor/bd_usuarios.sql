CREATE DATABASE bd_usuarios;
USE bd_usuarios;

CREATE TABLE usuarios(
    UsuarioId int not null AUTO_INCREMENT,
    Nombre varchar(100) NOT NULL,
    Clave varchar(100) NOT NULL,
    PRIMARY KEY (UsuarioId) 
);

INSERT INTO usuarios(Nombre, Clave)
VALUES("Pepito perez","12"),("Ricardo Jorge","13");