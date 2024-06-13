const db = require('../../database/database.db'); // Adjust the path to where your db instance is exported
const { emailExists, phoneExists, router } = require('../routes/signup'); // Adjust the path to where your function is exported
const request = require('supertest');
const express = require('express');

jest.mock('../../database/database.db', () => ({
  get: jest.fn(),
  run: jest.fn(),
}));

describe('emailExists', () => {
  it('should return true when the email exists', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(null, { someData: 1 }); // Simulate row returned
    });

    emailExists('arthursclarke@outlook.com', (result) => {
      expect(result).toBe(true);
      done();
    });
  });

  it('should return false when the email does not exist', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(null, null); // Simulate no row returned
    });

    emailExists('0', (result) => {
      expect(result).toBe(false);
      done();
    });
  });

  it('should return false when there is an error', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(new Error('Database error'), null); // Simulate an error
    });

    emailExists('test@example.com', (result) => {
      expect(result).toBe(false);
      done();
    });
  });
});

describe('phoneExists', () => {
  it('should return true when the phone exists', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(null, { someData: 1 }); // Simulate row returned
    });

    phoneExists('07521260287', (result) => {
      expect(result).toBe(true);
      done();
    });
  });

  it('should return false when the phone does not exist', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(null, null); // Simulate no row returned
    });

    phoneExists('0', (result) => {
      expect(result).toBe(false);
      done();
    });
  });

  it('should return false when there is an error', (done) => {
    db.get.mockImplementation((query, params, callback) => {
      callback(new Error('Database error'), null); // Simulate an error
    });

    phoneExists('1234567890', (result) => {
      expect(result).toBe(false);
      done();
    });
  });
});

// describe('POST /signup', () => {
//   let app;

//   beforeAll(() => {
//     app = express();
//     app.use(express.urlencoded({ extended: false }));
//     app.use('/', router);
//   });

//   it('should render an alert when no email or phone number is given', async () => {
//     const res = await request(app)
//       .post('/')
//       .send({ email: '', phoneNumber: '' });

//     expect(res.text).toContain('No email or phone number given');
//   });

//   it('should add data to the database when email and phone number are provided', async () => {
//     db.get.mockImplementation((query, params, callback) => {
//       callback(null, null); // Simulate no row returned
//     });

//     db.run.mockImplementation((query, params, callback) => {
//       callback(null); // Simulate successful insert
//     });

//     const res = await request(app)
//       .post('/')
//       .send({ email: 'test@example.com', phoneNumber: '1234567890' });

//     expect(db.run).toHaveBeenCalledTimes(2);
//     expect(db.run).toHaveBeenCalledWith("INSERT INTO OptedNumbers VALUES (?, 'km')", ['1234567890'], expect.any(Function));
//     expect(db.run).toHaveBeenCalledWith("INSERT INTO OptedEmails VALUES (?, 'km')", ['test@example.com'], expect.any(Function));
//   });
// });
