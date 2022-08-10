export default function updateStudentGradeByCity(
  studentArray,
  city,
  newGrades
) {
  if (!Array.isArray(studentArray)) return [];
  return studentArray
    .filter((student) => student.location === city)
    .map((student) => {
      const studentNewGrade = newGrades.find(
        (grade) => grade.studentId === student.id
      );
      if (typeof studentNewGrade === 'undefined') {
        return { ...student, grade: 'N/A' };
      }
      return { ...student, grade: studentNewGrade.grade };
    });
}
