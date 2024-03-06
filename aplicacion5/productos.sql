DROP TABLE IF EXISTS productos;

CREATE TABLE IF NOT EXISTS productos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT NOT NULL,
  precio DECIMAL(10, 2) NOT NULL,
  existencia INT NOT NULL
);

INSERT INTO productos (nombre, descripcion, precio, existencia) VALUES ('Apuntador', 'Apuntador Lazer', 100.00, 10);
INSERT INTO productos (nombre, descripcion, precio, existencia) VALUES ('Mause', 'Mause Lenovo', 150.00, 5);