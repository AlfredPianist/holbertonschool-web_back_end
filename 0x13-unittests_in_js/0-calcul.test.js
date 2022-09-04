const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('#calculateNumber()', () => {
  it('sums two integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(-10, 2), -8);
    assert.strictEqual(calculateNumber(-2, 0), -2);
  });
  it('rounds numbers on addition', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(3.7, 1), 5);
    assert.strictEqual(calculateNumber(3.7, 1.2), 5);
    assert.strictEqual(calculateNumber(3.7, 1.5), 6);
  });
  it('returns NaN when number of arguments is incorrect', () => {
    assert.strictEqual(isNaN(calculateNumber()), true);
    assert.strictEqual(isNaN(calculateNumber(1)), true);
  });
});
