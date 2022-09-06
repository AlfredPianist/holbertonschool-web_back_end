const expect = require('chai').expect;
const request = require('request');

describe('integration test', () => {
  describe('GET /', () => {
    it('has the correct output on GET / endpoint', () => {
      request.get('http://localhost:7865').on,
        ('response',
        (response) => {
          expect(response.statusCode).to.equal(200);
          expect(response.body).to.equal('Welcome to the payment system');
        });
    });
  });
});
