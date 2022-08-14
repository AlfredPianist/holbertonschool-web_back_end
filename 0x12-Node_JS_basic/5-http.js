const http = require('http');
const { argv } = require('process');
const countStudents = require('./3-read_file_async');

const app = http.createServer((request, response) => {
  const { url } = request;
  const database = argv[2];

  response.setHeader('Content-Type', 'text/plain');

  switch (url) {
    case '/':
      response.statusCode = 200;
      response.end('Hello Holberton School!');
      break;
    case '/students':
      response.write('This is the list of our students\n');
      countStudents(database)
        .then((message) => response.end(message.join('\n')))
        .catch((error) => response.end(error.message));
      break;
    default:
      response.statusCode = 404;
      response.end();
  }
});

app.listen(1245);

module.exports = app;
