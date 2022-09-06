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

  describe('GET /cart/:id', () => {
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

  describe('GET /available_payments', () => {
    it('has the correct output on GET /available_payments endpoint', (done) => {
      const call = {
        url: 'http://localhost:7865/available_payments',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.deep.equal(
          '{"payment_methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      });
    });

    it('has the correct output on GET /available_payments endpoint when parsed', (done) => {
      const call = {
        url: 'http://localhost:7865/available_payments',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });
        done();
      });
    });
  });

  describe('POST /login', () => {
    it('has the correct output on POST /login endpoint with body', (done) => {
      const call = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          userName: 'Alfredo',
        },
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.deep.equal('Welcome Alfredo');
        done();
      });
    });

    it('has the correct output on POST /login endpoint with no body', (done) => {
      const call = {
        url: 'http://localhost:7865/login',
        method: 'POST',
      };
      request(call, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.deep.equal('Welcome undefined');
        done();
      });
    });
  });
});
