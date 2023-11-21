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

