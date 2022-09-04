const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('#calculateNumber(), type = SUM', () => {
  it('has correct output', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM', 3.7, 1), 5);
    assert.strictEqual(calculateNumber('SUM', 3.7, 1.2), 5);
    assert.strictEqual(calculateNumber('SUM', 3.7, 1.5), 6);
  });
});

describe('#calculateNumber(), type = SUBTRACT', () => {
  it('has correct output', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
  });
});

describe('#calculateNumber(), type = DIVIDE', () => {
  it('has correct output', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 0.0, 1), 0);
    assert.strictEqual(calculateNumber('DIVIDE', 2, 2.5), 0.6666666666666666);
    assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
  });

  it('outputs error when divisor is 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 10.7, 0.2), 'Error');
  });
});
