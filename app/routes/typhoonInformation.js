const express = require('express');
const router = express.Router();

router.get('/typhoonInformation', (req, res) => {
  res.render('typhoonInformation');
});

console.log("Creating routes to: typhoonInformation");
module.exports = router;