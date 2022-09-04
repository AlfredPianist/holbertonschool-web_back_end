'use strict';
const Utils = require('./utils.js');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
};
module.exports = sendPaymentRequestToApi;
