# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY gateway.js ./

# Install dependencies
RUN npm install

# Expose the port that the application will run on
EXPOSE 3000

# Command to run the application
CMD ["node", "gateway.js"]
