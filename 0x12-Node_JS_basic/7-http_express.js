const express = require('express');
const { argv } = require('process');
const countStudents = require('./3-read_file_async');

const app = express();
const database = argv[2];

app.get('/', (request, response) => response.send('Hello Holberton School!'));
app.get('/students', (request, response) => {
  const responseArray = [];
  responseArray.push('This is the list of our students');
  countStudents(database)
    .then((message) => {
      responseArray.push(message);
      response.send(responseArray.join('\n'));
    })
    .catch((error) => {
      responseArray.push(error);
      response.send(responseArray.join('\n'));
    });
});

app.listen(1245);

module.exports = app;
