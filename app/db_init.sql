-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS agenda_db;
USE agenda_db;

-- Tabla que almacena los contactos de la agenda:
CREATE TABLE contactos (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(50) NOT NULL,
  telefono varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Tabla que almacena los usuarios que se registran en la aplicación:
CREATE TABLE usuarios (
  username varchar(45) NOT NULL,
  name varchar(255) NOT NULL,
  surname varchar(255) DEFAULT NULL,
  email varchar(320) NOT NULL,
  password_hash varchar(255) NOT NULL,
  PRIMARY KEY (`username`)
);

-- Insertamos un set de contactos de ejemplo:
INSERT INTO contactos (nombre, telefono) VALUES ('Juan', '123');
INSERT INTO contactos (nombre, telefono) VALUES ('Pedro', '456');
INSERT INTO contactos (nombre, telefono) VALUES ('María', '789');

-- Insertamos un usuario de prueba (contraseña 1234):
INSERT INTO usuarios (username, name, surname, email, password_hash) VALUES ('admin', 'Admin', 'Admin', 'admin@iesciudadjardin.com','scrypt:32768:8:1$nvPXYbFk3TGZ2791$e1976f513f488e4d66ddfbce71c0aab0801b23930781f85218863f62e7689769ff3875d35a28962d9593e011da7a7c6092fdcbc7577855ed44f40363e76b034c');