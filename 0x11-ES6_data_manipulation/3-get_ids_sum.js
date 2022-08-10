export default function getStudentIdsSum(studentArray) {
  if (!Array.isArray(studentArray)) return [];
  return studentArray.reduce((sum, student) => sum + student.id, 0);
}
