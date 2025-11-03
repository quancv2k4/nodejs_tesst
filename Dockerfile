FROM node:20-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy application
COPY . .

# Build if needed (TypeScript, etc.)
RUN npm run build || echo "No build needed"

# Expose port
EXPOSE 8000

# Run application
CMD ["node", "server.js"]