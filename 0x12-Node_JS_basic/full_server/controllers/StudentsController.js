import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response, DATABASE) {
    readDatabase(DATABASE)
      .then((fields) => {
        const studentsMessage = [];

        for (const field of Object.keys(fields)) {
          studentsMessage.push(
            `Number of students in ${field}: ${
              fields[field].length
            }. List: ${fields[field].join(', ')}`
          );
        }

        response.status(200).send(`${studentsMessage.join('\n')}`);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response, DATABASE) {
    const { major } = request.params;
    const majors = ['CS', 'SWE'];

    if (!majors.includes(major)) {
      response.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase(DATABASE)
        .then((fields) => {
          response.status(200).send(`List: ${fields[major].join(', ')}`);
        })
        .catch(() => response.status(500).send('Cannot load the database'));
    }
  }
}
