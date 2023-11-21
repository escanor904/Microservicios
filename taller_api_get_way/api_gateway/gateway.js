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
      port: 9092,
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

const logResponse = (req,res) => {
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
app.get('/mostrarPerfil', async (req, res) => {
  try {
    const receivedToken = req.headers.authorization; // Recibe el token desde el encabezado

    if (!receivedToken) {
      return res.status(400).json({ error: 'Falta el token en el encabezado' });
    }

    // Envía el token a la otra aplicación en el encabezado
    const otherAppURL = 'http://127.0.0.1:8080/getProfile'; // Reemplaza con la URL real
    await axios.get(otherAppURL, {
      headers: {
        Authorization: receivedToken, // Incluir el token en el encabezado
      },
    });

    res.json({ message: 'Token enviado correctamente' });
  } catch (error) {
    console.error('Error sending token:', error);
    res.status(500).json({ error: 'Error al enviar el token' });
  }
});

app.put('/updateProfile', async (req, res) => {
  try {
    const { username, personalpage, biography, organization, country, linkedinUrl, publicInformation } = req.body;
    const token = req.headers.authorization; // Obtener el token del encabezado

    if (!token) {
      return res.status(400).json({ error: 'Falta el token en la solicitud' });
    }

    // Envía el token y otros datos a otra API
    const otherApiURL = 'http://127.0.0.1:8080/updateProfile'; // Reemplaza con la URL real
    await axios.put(
      otherApiURL,
      { username, personalpage, biography, organization, country, linkedinUrl, publicInformation },
      {
        headers: {
          Authorization: token, // Incluir el token en el encabezado
        },
      }
    );

    res.json({ message: 'Datos almacenados y enviados correctamente' });
  } catch (error) {
    console.error('Error processing request:', error);

    res.status(500).json({ error: 'Error al procesar la solicitud' });
  }
});

app.listen(PORT, () => {
  console.log(`API Gateway Funcionando En El Puerto ${PORT}`);
});


//---------------------------------Rutas salud----------------------------------------------
// Ruta para verificar la salud del servicio
app.get('/health', (req, res) => {
  res.status(200).json({ message: 'Health check OK' });
});

// Ruta para verificar el estado "live" del servicio
app.get('/health/live', (req, res) => {
  res.status(200).json({ message: 'Live' });
});

// Ruta para verificar la disponibilidad del servicio
app.get('/health/ready', async (req, res) => {
  const verificar_endpoints = verificar_endpoints; 


  if (verificar_endpoints) {
    res.status(200).json({ status: 'Ready' });
  } else {
    res.status(503).json({ status: 'Not Ready' });
  }
});

const urls = [
  'http://127.0.0.1:5000/inicio_sesion',
  'http://127.0.0.1:5000/users',
  'http://127.0.0.1:8080/getProfile',
  'http://127.0.0.1:8080/updateProfile'
];

async function verificar_endpoints() {
  const results = await Promise.all(
    urls.map(async url => {
      try {
        const response = await axios.get(url);
        if (response.status === 200) {
          return { url, status: 'Disponible' };
        } else {
          return { url, status: 'Respondió, pero con un código de estado diferente a 200' };
        }
      } catch (error) {
        return { url, status: 'Error al intentar acceder al endpoint' };
      }
    })
  );

  results.forEach(result => {
    console.log(`Endpoint: ${result.url} - Estado: ${result.status}`);
  });
}

//---------------------------------Rutas salud----------------------------------------------
// Ruta para verificar la salud del servicio
app.get('/health', (req, res) => {
  res.status(200).json({ message: 'Health check OK' });
});

// Ruta para verificar el estado "live" del servicio
app.get('/health/live', (req, res) => {
  res.status(200).json({ message: 'Live' });
});

// Ruta para verificar la disponibilidad del servicio
app.get('/health/ready', async (req, res) => {
  const verificar_endpoints = verificar_endpoints; 


  if (verificar_endpoints) {
    res.status(200).json({ status: 'Ready' });
  } else {
    res.status(503).json({ status: 'Not Ready' });
  }
});

const urls = [
  'http://127.0.0.1:5000/inicio_sesion',
  'http://127.0.0.1:5000/users',
  'http://127.0.0.1:8080/getProfile',
  'http://127.0.0.1:8080/updateProfile'
];

async function verificar_endpoints() {
  const results = await Promise.all(
    urls.map(async url => {
      try {
        const response = await axios.get(url);
        if (response.status === 200) {
          return { url, status: 'Disponible' };
        } else {
          return { url, status: 'Respondió, pero con un código de estado diferente a 200' };
        }
      } catch (error) {
        return { url, status: 'Error al intentar acceder al endpoint' };
      }
    })
  );

  results.forEach(result => {
    console.log(`Endpoint: ${result.url} - Estado: ${result.status}`);
  });
}

