const expect = require('chai').expect;
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('#sendPaymentRequestToApi()', () => {
  let spy;
  beforeEach(() => (spy = sinon.spy(console, 'log')));
  afterEach(() => spy.restore());

  it("has the correct output from the Utils.calculateNumber('SUM', 100, 20) function", () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('The total is: 120')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });

  it("has the correct output from the Utils.calculateNumber('SUM', 10, 10) function", () => {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledWith('The total is: 20')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
});
