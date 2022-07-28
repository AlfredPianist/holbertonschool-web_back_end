export default function createIteratorObject(report) {
  return { [Object.keys(report)]: { ...report } };
}
