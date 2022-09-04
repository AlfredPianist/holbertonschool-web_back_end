const calculateNumber = require('./2-calcul_chai');
const expect = require('chai').expect;

describe('#calculateNumber(), type = SUM', () => {
  it('has correct output', () => {
    expect(calculateNumber('SUM', 1, 3.7)).to.be.a('number');
    expect(calculateNumber('SUM', 1, 3.7)).to.be.equal(5);
    expect(calculateNumber('SUM', 3.7, 1)).to.be.a('number');
    expect(calculateNumber('SUM', 3.7, 1)).to.be.equal(5);
  });
});

describe('#calculateNumber(), type = SUBTRACT', () => {
  it('has correct output', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.be.a('number');
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.be.equal(-3);
    expect(calculateNumber('SUBTRACT', 3.7, 1)).to.be.a('number');
    expect(calculateNumber('SUBTRACT', 3.7, 1)).to.be.equal(3);
  });
});

describe('#calculateNumber(), type = DIVIDE', () => {
  it('has correct output', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.a('number');
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.equal(0.2);
  });

  it('outputs error when divisor is 0', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.be.a('string');
    expect(calculateNumber('DIVIDE', 1, 0)).to.be.equal('Error');
    expect(calculateNumber('DIVIDE', 10.7, 0.2)).to.be.equal('Error');
  });
});
