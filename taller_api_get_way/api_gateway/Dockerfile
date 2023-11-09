# Usamos la imagen base de Node.js
FROM node:latest

# Establecemos el directorio de trabajo en la aplicación
WORKDIR /app

#Actualizamos
RUN apt-get update && apt-get upgrade -y
RUN apt-get install npm

# Instalamos las dependencias
RUN npm install express
RUN npm install axios
RUN npm install winston

# Copiamos el resto de los archivos de la aplicación
COPY . .

# Exponemos el puerto 3000 (el puerto en el que la app está escuchando)
EXPOSE 3000

# Comando para iniciar la aplicación cuando se ejecute el contenedor
CMD ["node", "gateway.js"]
