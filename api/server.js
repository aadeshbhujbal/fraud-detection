const express = require('express');
const app = express();
const port = process.env.API_PORT || 3001;

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.listen(port, () => {
  console.log(`API server listening at http://localhost:${port}`);
}); 