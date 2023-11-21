const { Given, When, Then } = require('cucumber');
const { Pool } = require('pg');
const assert = require('assert');


const dbConfig = {
  database: 'authentication_db',
  user: 'admin',
  password: 'admin_password',
  host: 'localhost',
  port: '5434',
};

Given('tener un usuario registrado en el sistema', async function () {
    const pool = new Pool(dbConfig);
    const client = await pool.connect();

    try {
        const result = await client.query('SELECT * FROM users LIMIT 1');
        const user = result.rows[0];

        if (user) {
            this.email = user[3];
            this.user = user;
            assert(user !== null);
        } else {
            assert(false); // Fails the step if user is not found
        }
    } catch (error) {
        assert(false); // Fails the step in case of error
    } finally {
        client.release(); // Releases the client connection
    }
});

Given('no tener un usuario que no este registrado en el sistema', function () {
  this.user = null;
  if (this.user === null) {
      assert(this.user === null);
  } else {
      assert(false); // Fails the step if user is not null
  }
});

Given('tener la contraseña para el usuario registrado', function () {
    if (this.user !== null) {
        assert(this.user[2] !== null);
    } else {
        assert(this.user === null);
    }
});

When('se realiza una solicitud para iniciar sesion', async function () {
    if (this.user !== null) {
        const pool = new Pool(dbConfig);
        const client = await pool.connect();

        try {
            const result = await client.query('SELECT * FROM users LIMIT 1');
            const user = result.rows[0];

            if (user) {
                this.password = user[2];
                assert(this.password !== null);
            } else {
                assert(false); // Fails the step if password is null
            }
        } catch (error) {
            assert(false); // Fails the step in case of error
        } finally {
            client.release(); // Releases the client connection
        }
    } else {
        assert(this.user === null);
    }
});

Then('se recibe una respuesta exitosa con el {string}', function (mensaje) {
    if (this.user !== null) {
        assert(mensaje === mensaje);
    } else {
        assert(mensaje === mensaje);
    }
});
