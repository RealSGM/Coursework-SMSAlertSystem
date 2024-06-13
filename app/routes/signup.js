const express = require('express');
const router = express.Router();
const sqlite3 = require('sqlite3').verbose();
// const db = new sqlite3.Database('../../database/database.db');
const db = new sqlite3.Database('../database/database.db');

router.get('/', (req, res) => {
  res.render('signup', {alert: ""});
});

console.log("Creating routes to: signup");

function emailExists(email, callback) {
  db.get("SELECT 1 FROM OptedEmails WHERE Email = ?", [email], (err, row) => {
    if (err) {
      console.error(err);
      callback(false); // If an error occurs, assume the email does not exist
    } else {
      callback(!!row); // If a row is returned, the email exists
    }
  });
}



function phoneExists(phone, callback) {
  db.get("SELECT 1 FROM OptedNumbers WHERE PhoneNumber = ?", [phone], (err, row) => {
    if (err) {
      console.error(err);
      callback(false); // If an error occurs, assume the phone number does not exist
    } else {
      callback(!!row); // If a row is returned, the phone number exists
    }
  });
}

router.post('/', (req, res, next) => {
  var email = req.body.email;
  var phone = req.body.phoneNumber;
  console.log(email, phone);
  
  if (email === "" && phone === "") {
    res.render('signup', {alert: "មិនបានផ្តល់អ៊ីមែល ឬលេខទូរស័ព្ទទេ។"});
  } else {
    emailExists(email, (emailExists) => {
      phoneExists(phone, (phoneExists) => {
        if (emailExists || phoneExists) {
          res.render('signup', {alert: "អ៊ីមែល ឬលេខទូរស័ព្ទនេះត្រូវបានប្រើប្រាស់រួចហើយ។"});
        } else {
          db.run("INSERT INTO OptedNumbers VALUES (?, 'km')", [phone], (err) => {
            if (err) {
              console.error(err);
              res.render('signup', {alert: "កំហុស​មួយ​បាន​កើត​ឡើង"});
            } else {
              db.run("INSERT INTO OptedEmails VALUES (?, 'km')", [email], (err) => {
                if (err) {
                  console.error(err);
                  res.render('signup', {alert: "កំហុស​មួយ​បាន​កើត​ឡើង"});
                } else {
                  res.render('signup', {alert: "ព័ត៌មានលម្អិតដែលបានចុះឈ្មោះ"});
                }
              });
            }
          });
        }
      });
    });
  }
});

module.exports = router;



// function sum(a, b) {
//   return a + b;
// }
// module.exports = sum;
//module.exports = { emailExists, phoneExists, router };