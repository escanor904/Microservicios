-- Creación de la tabla logs
CREATE TABLE logs (
  log_id BIGSERIAL PRIMARY KEY,
  nombre_app VARCHAR(50) NOT NULL,
  tipo_log VARCHAR(30) NOT NULL,
  fecha_log TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  descripcion VARCHAR(100) NOT NULL,
  user_email VARCHAR(100) NOT NULL
);

-- Inserción de datos de prueba en la tabla logs
INSERT INTO logs (nombre_app, tipo_log, descripcion, user_email) VALUES
  ('application', 'log_type', 'description', 'user_email@example.com');x