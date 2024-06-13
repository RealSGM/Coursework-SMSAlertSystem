const express = require('express');
const router = express.Router();

router.get('/floodInformation', (req, res) => {
  res.render('floodInformation');
});

console.log("Creating routes to: floodInformation");
module.exports = router;