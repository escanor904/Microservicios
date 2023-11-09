const express = require('express');
const axios = require('axios');
const winston = require('winston');

const app = express();
const PORT = 3000;

// Configuración de Winston para enviar logs a un API o servicio centralizado
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'api-gateway' },
  transports: [
    new winston.transports.Http({
      host: 'URL_DEL_API_DE_LOGS_CENTRALIZADO', // Reemplaza con la URL de tu API de logs
      port: 80, // Puerto del API de logs
      path: '/log', // Ruta para enviar los logs al API
    }),
  ],
});

// Middleware para registrar logs
const logMiddleware = (req, res, next) => {
  logger.info(`${req.method} Request for ${req.url}`);
  next();
};

app.use(express.json());
app.use(logMiddleware);

// Ruta para autenticación
app.post('/auth', async (req, res) => {
    const { email, password } = req.body;
  
    if (!email || !password) {
      return res.status(400).json({ error: 'Faltan datos de email o contraseña' });
    }
  
    try {
      const authResponse = await axios.post('URL_DEL_API_DE_AUTENTICACION', {
        email,
        password,
      });
  
      res.json(authResponse.data);
    } catch (error) {
      res.status(500).json({ error: 'Error en la autenticación' });
    }
  });

// Ruta para registro
app.post('/register', async (req, res) => {
    const { username, password, email } = req.body;
  
    if (!username || !password || !email) {
      return res.status(400).json({ error: 'Faltan datos de nombre de usuario, contraseña o email' });
    }
  
    try {
      const registerResponse = await axios.post('URL_DEL_API_DE_REGISTRO', {
        username,
        password,
        email,
      });
  
      res.json(registerResponse.data);
    } catch (error) {
      res.status(500).json({ error: 'Error en el registro' });
    }
  });

  app.listen(PORT, () => {
    console.log(`API Gateway FUncionando En El Puerto ${PORT}`);
  });
