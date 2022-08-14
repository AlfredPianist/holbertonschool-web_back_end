const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const message = [];
      const dataDumpArray = data.split('\n');
      const fields = {};

      const studentArray = dataDumpArray
        .filter((row) => row)
        .map((row) => row.split(','));
      studentArray.shift();

      studentArray.forEach((student) => {
        if (!fields[student[3]]) {
          fields[student[3]] = [];
        }
        fields[student[3]].push(student[0]);
      });

      message.push(`Number of students: ${studentArray.length}`);
      for (const [fieldName, fieldStudents] of Object.entries(fields)) {
        message.push(
          `Number of students in ${fieldName}: ${
            fieldStudents.length
          }. List: ${fieldStudents.join(', ')}`,
        );
      }

      const response = message.join('\n');
      console.log(response);
      resolve(response);
    });
  });
}

module.exports = countStudents;
