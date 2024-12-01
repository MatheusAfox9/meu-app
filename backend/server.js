// backend/server.js

const express = require('express');
const app = express();
const port = 3000;

// Definindo uma rota simples
app.get('/', (req, res) => {
  res.send('Bem-vindo à API backend com Express!');
});

// Iniciando o servidor na porta definida
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
