const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI()', () => {
  it('returns done after promise is resolved', (done) => {
    getPaymentTokenFromAPI(true)
      .then((result) => {
        expect(result).to.include({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error));
  });
});
