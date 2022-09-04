const calculateNumber = (type, a, b) => {
  const rounded_a = Math.round(a);
  const rounded_b = Math.round(b);
  switch (type) {
    case 'SUM':
      return rounded_a + rounded_b;
    case 'SUBTRACT':
      return rounded_a - rounded_b;
    case 'DIVIDE':
      if (b === 0) {
        return 'Error';
      }
      return rounded_a / rounded_b;
  }
};
module.exports = calculateNumber;
