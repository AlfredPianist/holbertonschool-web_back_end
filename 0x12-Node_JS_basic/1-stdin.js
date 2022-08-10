const { stdin, stdout } = require('process');

stdout.write('Welcome to Holberton School, what is your name?\n');
stdin.on('readable', () => {
  const data = stdin.read();
  if (data !== null) {
    stdout.write(`Your name is: ${data.toString()}`);
  }
});
stdin.on('end', () => {
  stdout.write('This important software is now closing\n');
});
