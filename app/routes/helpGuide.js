const express = require('express');
const router = express.Router();

router.get('/helpGuide', (req, res) => {
  res.render('helpGuide');
});

console.log("Creating routes to: helpGuide");
module.exports = router;