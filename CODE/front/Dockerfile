# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias de la aplicación
RUN bun install

# Copia el resto de la aplicación al contenedor
COPY . .

# Expón el puerto en el que la aplicación se ejecutará
EXPOSE 5174

# Comando para iniciar la aplicación
CMD ["bun", "run","dev"]
