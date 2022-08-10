const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const dataArray = data.split('\n');
      const keys = dataArray[0].split(',');
      const objectArray = [];
      const message = [];

      for (let lineIdx = 1; lineIdx < dataArray.length; lineIdx += 1) {
        const row = dataArray[lineIdx].split(',');
        if (row.length >= keys.length) {
          const object = {};
          for (let valueIdx = 0; valueIdx < keys.length; valueIdx += 1) {
            object[keys[valueIdx]] = row[valueIdx];
          }
          objectArray.push(object);
        }
      }

      const fields = {};
      objectArray.forEach((row) => {
        if (typeof fields[row.field] === 'undefined') {
          fields[row.field] = {};
          fields[row.field].count = 0;
          fields[row.field].studentList = [];
        }
        fields[row.field].count += 1;
        fields[row.field].studentList.push(row.firstname);
      });

      message.push(`Number of students: ${objectArray.length}`);
      for (const [fieldName, fieldInfo] of Object.entries(fields)) {
        message.push(
          `Number of students in ${fieldName}: ${
            fieldInfo.count
          }. List: ${fieldInfo.studentList.join(', ')}`,
        );
      }

      const response = message.join('\n');
      console.log(response);
      resolve(response);
    });
  });
}

module.exports = countStudents;
