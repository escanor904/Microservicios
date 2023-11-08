const express = require('express');
const axios = require('axios');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Middleware para registrar logs
const logMiddleware = (req, res, next) => {
  const logData = `${new Date().toISOString()} - ${req.method} Request for ${req.url}\n`;
  fs.appendFile('logs.txt', logData, (err) => {
    if (err) console.error('Error writing to log file');
  });
  next();
};

app.use(express.json());
app.use(logMiddleware);

// Ruta para autenticación
app.post('/auth', async (req, res) => {
  try {
    const authResponse = await axios.post('URL_DEL_API_DE_AUTENTICACION', req.body);
    res.json(authResponse.data);
  } catch (error) {
    res.status(500).json({ error: 'Error en la autenticación' });
  }
});

// Ruta para registro
app.post('/register', async (req, res) => {
  try {
    const registerResponse = await axios.post('URL_DEL_API_DE_REGISTRO', req.body);
    res.json(registerResponse.data);
  } catch (error) {
    res.status(500).json({ error: 'Error en el registro' });
  }
});

app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});
