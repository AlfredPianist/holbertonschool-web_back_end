const expect = require('chai').expect;
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('#sendPaymentRequestToApi()', () => {
  const spy = sinon.spy(console, 'log');

  it('has the correct output from the Utils.calculateNumber function', () => {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('The total is: 10')).to.be.true;
    expect(spy.calledOnce).to.be.true;
    spy.restore;
    stub.restore;
  });
});
