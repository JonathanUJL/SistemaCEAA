-- Crear base de datos
CREATE DATABASE gestion_documentos;

-- Usar la base de datos
USE gestion_documentos;

-- Crear tabla de áreas administrativas
CREATE TABLE areas_administrativas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    area_id INT,
    FOREIGN KEY (area_id) REFERENCES areas_administrativas(id)
);

-- Crear tabla de documentos
CREATE TABLE documentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    contenido TEXT NOT NULL,
    usuario_id INT,
    area_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (area_id) REFERENCES areas_administrativas(id)
) ENGINE=InnoDB;
