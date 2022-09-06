const expect = require('chai').expect;
const request = require('request');

describe('integration test', () => {
  describe('GET /', () => {
    it('has the correct output on GET /cart/:id endpoint', (done) => {
      const call = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });

    it('has the correct output on GET /cart/:id endpoint when :id is not a number', (done) => {
      const call = {
        url: 'http://localhost:7865/cart/nan',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
