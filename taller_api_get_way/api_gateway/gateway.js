const express = require('express');
const axios = require('axios');
const winston = require('winston');

const app = express();
const PORT = 3000;

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  defaultMeta: { service: 'api-gateway' },
  transports: [
    new winston.transports.Http({
      host: '127.0.0.1',
      port: 5000,
      path: '/log',
    }),
  ],
});

const logMiddleware = (req, res, next) => {
  const startTime = new Date();
  req.startTime = startTime;

  // Log simple en la consola
  console.log(`Received ${req.method} request for ${req.url}`);

  next();
};

const logResponse = (req, res) => {
  let logInfo = {
    application: 'api-gateway', // Nombre de la aplicación
    log_type: 'info', // Tipo de log (puedes personalizar esto según tus necesidades)
    timestamp: new Date().toISOString(),
    description: `${req.method} Request for ${req.url}`, // Descripción de la solicitud
    email: req.body.email || '', // Correo electrónico (si está presente en el cuerpo de la solicitud)
  };

  logger.info(logInfo);
};

app.use(express.json());
app.use(logMiddleware);

app.post('/auth', async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: 'Faltan datos de email o contraseña' });
    }

    const authResponse = await axios.post('http://127.0.0.1:5000/inicio_sesion', { email, password });

    logResponse(req, res);

    res.json(authResponse.data);
  } catch (error) {
    logResponse(req, res);

    res.status(500).json({ error: 'Error en la autenticación' });
  }
});

app.post('/register', async (req, res) => {
  try {
    const { username, password, email } = req.body;

    if (!username || !password || !email) {
      return res.status(400).json({ error: 'Faltan datos de nombre de usuario, contraseña o email' });
    }

    const registerResponse = await axios.post('http://127.0.0.1:5000/users', { username, password, email });

    logResponse(req, res);

    res.json(registerResponse.data);
  } catch (error) {
    logResponse(req, res);

    res.status(500).json({ error: 'Error en el registro' });
  }
});

app.use(express.json());
app.use(logMiddleware);

// Ruta para recibir y reenviar el token
app.get('/mostrarPerfil', (req, res) => {
  try {
    const receivedToken = req.query.token; // Recibe el token desde la variable de consulta

    if (!receivedToken) {
      return res.status(400).json({ error: 'Falta el token en la variable de consulta' });
    }

    // Envía el token a la otra aplicación
    const otherAppURL = 'http://127.0.0.1:8080/getProfile'; // Reemplaza con la URL real
    axios.post(otherAppURL, { token: receivedToken });

    res.json({ message: 'Token enviado correctamente' });
  } catch (error) {
    res.status(500).json({ error: 'Error al enviar el token' });
  }
});

app.update('/updateProfile', async (req, res) => {
  try {
    const { token, username, personalpage, correspondence, biography, organization, country, linkedinUrl, publicInformation } = req.body;

    if (!token) {
      return res.status(400).json({ error: 'Falta el token en la solicitud' });
    }

    // Log al recibir datos
    let logInfoReceive = {
      application: 'api-gateway',
      log_type: 'info',
      timestamp: new Date().toISOString(),
      description: 'Received bad data for storage'
    };
    logger.info(logInfoReceive);

    // Envía el token y otros datos a otra API
    const otherApiURL = 'http://127.0.0.1:8080/updateProfile'; // Reemplaza con la URL real
    await axios.post(otherApiURL, { token, username, personalpage, correspondence, biography, organization, country, linkedinUrl, publicInformation });

    // Log al enviar datos a otra API
    let logInfoSend = {
      application: 'api-gateway',
      log_type: 'info',
      timestamp: new Date().toISOString(),
      description: 'Sent data to another API',
      data: { username, personalpage, correspondence, biography, organization, country, linkedinUrl, publicInformation },
    };
    logger.info(logInfoSend);

    res.json({ message: 'Datos almacenados y enviados correctamente' });
  } catch (error) {
    // Log en caso de error
    let logError = {
      application: 'api-gateway',
      log_type: 'error',
      timestamp: new Date().toISOString(),
      description: 'Error processing the request',
      error: error.message,
    };
    logger.error(logError);

    res.status(500).json({ error: 'Error al procesar la solicitud' });
  }
});

app.listen(PORT, () => {
  console.log(`API Gateway Funcionando En El Puerto ${PORT}`);
});
