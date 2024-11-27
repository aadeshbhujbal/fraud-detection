const express = require('express');
const { Kafka } = require('kafkajs');
const { Client } = require('@elastic/elasticsearch');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

// Start server
app.listen(port, () => {
  console.log(`API server listening at http://localhost:${port}`);
}); 