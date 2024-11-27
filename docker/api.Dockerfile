FROM node:18-slim

WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY src/ ./src/

ENV PORT=3000
EXPOSE 3000

CMD ["node", "src/index.js"] 