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
      const keys = dataDumpArray[0].split(',');
      const fields = {};

      const studentArray = dataDumpArray.map((row) => {
        const studentRow = row.split(',');
        const student = {};
        for (const [keyIdx, key] of keys.entries()) {
          student[key] = studentRow[keyIdx];
        }
        return student;
      });
      studentArray.shift();

      studentArray.forEach((student) => {
        if (typeof fields[student.field] === 'undefined') {
          fields[student.field] = {};
          fields[student.field].count = 0;
          fields[student.field].studentList = [];
        }
        fields[student.field].count += 1;
        fields[student.field].studentList.push(student.firstname);
      });

      message.push(`Number of students: ${studentArray.length}`);
      for (const [fieldName, fieldInfo] of Object.entries(fields)) {
        message.push(
          `Number of students in ${fieldName}: ${
            fieldInfo.count
          }. List: ${fieldInfo.studentList.join(', ')}`
        );
      }

      const response = message.join('\n');
      console.log(response);
      resolve(studentArray);
    });
  });
}

module.exports = countStudents;
