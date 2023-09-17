-- Usamos la base de datos --
USE estudiantes_bbdd;

-- Insertamos datos --
INSERT INTO alumnos (id_alumno, nombre, apellido, edad) VALUES (1, "Elián", "Ibarra", 12);
INSERT INTO alumnos (id_alumno, nombre, apellido, edad) VALUES (2, "Cristiano", "Ronaldo", 38);

-- Seleccionamos todos los registros de la tabla usuarios --
SELECT * FROM alumnos;

-- Seleccionamos los registros con nombre y edad, donde el valor de edad sea mayor a 18 --
SELECT nombre, edad FROM ALUMNOS WHERE edad > 18;