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
      host: '127.0.0.',
      port: 5000,
      path: '/log',
    }),
  ],
});

const logMiddleware = (req, res, next) => {
  const startTime = new Date();
  req.startTime = startTime;
  next();
};

const logResponse = (req, res) => {
  let logInfo = {
    application: req.path.slice(1),
    message: `${req.method} Request for ${req.url}`,
    timestamp: new Date().toISOString(),
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

app.listen(PORT, () => {
  console.log(`API Gateway Funcionando En El Puerto ${PORT}`);
});
