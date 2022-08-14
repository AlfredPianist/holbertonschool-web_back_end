function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const dataArray = data.split('\n');
      const keys = dataArray[0].split(',');
      const objectArray = [];
      const fieldsObject = {};

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

      objectArray.forEach((row) => {
        if (typeof fieldsObject[row.field] === 'undefined') {
          fieldsObject[row.field] = {};
          fieldsObject[row.field].studentList = [];
        }
        fieldsObject[row.field].studentList.push(row.firstname);
      });

      resolve(fieldsObject);
    });
  });
}
