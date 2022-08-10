export default function cleanSet(set, startString) {
  if (typeof startString === 'undefined') return '';
  if (typeof set !== 'object') return '';
  if (startString.length === 0) return '';

  const result = [];
  set.forEach((string) => {
    if (typeof string === 'string' && string.startsWith(startString)) {
      result.push(string.replace(startString, ''));
    }
  });
  return result.join('-');
}
