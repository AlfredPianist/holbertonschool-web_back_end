export default function updateUniqueItems(groceryList) {
  try {
    groceryList.forEach((value, key) => {
      if (value === 1) groceryList.set(key, 100);
    });
  } catch (error) {
    throw Error('Cannot process');
  }
}
