import { readFile } from 'fs';

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(Error(error));
        return;
      }

      const content = data.toString().split('\n');
      const fieldsObject = {};

      const students = content
        .filter((item) => item)
        .map((item) => item.split(','));
      students.shift();

      for (const student of students) {
        if (!fieldsObject[student[3]]) fieldsObject[student[3]] = [];
        fieldsObject[student[3]].push(student[0]);
      }

      resolve(fieldsObject);
    });
  });
}

export default readDatabase;
