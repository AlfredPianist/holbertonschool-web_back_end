const expect = require('chai').expect;
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('#sendPaymentRequestToApi()', () => {
  const spy = sinon.spy(Utils, 'calculateNumber');

  it('has the correct output from the Utils.calculateNumber function', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    expect(spy.calledOnce).to.be.true;
    spy.restore;
  });
});
