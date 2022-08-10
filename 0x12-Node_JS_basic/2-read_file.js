const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').split('\n');
    const keys = data[0].split(',');
    const objectArray = [];

    for (let lineIdx = 1; lineIdx < data.length; lineIdx++) {
      const object = {};
      const row = data[lineIdx].split(',');
      for (let valueIdx = 0; valueIdx < row.length; valueIdx++) {
        object[keys[valueIdx]] = row[valueIdx];
      }
      objectArray.push(object);
    }

    fields = {};
    objectArray.forEach((row) => {
      if (typeof fields[row.field] === 'undefined') {
        fields[row.field] = {};
        fields[row.field].count = 0;
        fields[row.field].studentList = [];
      }
      fields[row.field].count += 1;
      fields[row.field].studentList.push(row.firstname);
    });

    console.log(`Number of students: ${objectArray.length}`);
    for (const [fieldName, fieldInfo] of Object.entries(fields)) {
      console.log(
        `Number of students in ${fieldName}: ${
          fieldInfo.count
        }. List: ${fieldInfo.studentList.join(', ')}`
      );
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
