const express = require('express');
const router = express.Router();

router.get('/droughtInformation', (req, res) => {
  res.render('droughtInformation');
});
console.log("Creating routes to: droughtInformation");
module.exports = router;