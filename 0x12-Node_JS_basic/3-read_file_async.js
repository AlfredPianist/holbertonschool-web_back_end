const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const content = data.toString().split('\n');
      const fields = {};
      const response = [];
      let msg;

      const students = content
        .filter((item) => item)
        .map((item) => item.split(','));
      students.shift();

      const NUMBER_OF_STUDENTS = students.length ? students.length : 0;
      msg = `Number of students: ${NUMBER_OF_STUDENTS}`;
      console.log(msg);
      response.push(msg);

      for (const student of students) {
        if (!fields[student[3]]) fields[student[3]] = [];
        fields[student[3]].push(student[0]);
      }

      for (const field of Object.keys(fields)) {
        msg = `Number of students in ${field}: ${
          fields[field].length
        }. List: ${fields[field].join(', ')}`;

        console.log(msg);
        response.push(msg);
      }
      resolve(response);
    });
  });
}

module.exports = countStudents;
