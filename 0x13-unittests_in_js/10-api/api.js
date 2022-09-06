'use strict';
const express = require('express');
const app = express();
const port = 7865;

app.get('/', (request, response) =>
  response.end('Welcome to the payment system')
);

app.get('/cart/:id([0-9]+)', (request, response) =>
  response.end(`Payment methods for cart ${request.params.id}`)
);

app.get('/available_payments', (request, response) => {
  const payment_methods = {
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  };
  response.json(payment_methods);
});

app.post('/login', (request, response) => {
  const username = request.body.useName;
  response.end(`Welcome ${username}`);
});

app.get('/cart/:id([0-9]+)', (request, response) =>
  response.end(`Payment methods for cart ${request.params.id}`)
);

app.listen(port, () => console.log(`API available on localhost port ${port}`));
