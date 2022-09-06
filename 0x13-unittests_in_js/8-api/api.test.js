const expect = require('chai').expect;
const request = require('request');

describe('integration test', () => {
  describe('GET /', () => {
    it('has the correct output on GET / endpoint', (done) => {
      const call = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
