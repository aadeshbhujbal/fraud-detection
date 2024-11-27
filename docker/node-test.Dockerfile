FROM node:16

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Default command (can be overridden)
CMD ["npm", "test"] 