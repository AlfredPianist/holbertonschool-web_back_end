export default function setFromArray(set, array) {
  return array.every((n) => set.has(n));
}
