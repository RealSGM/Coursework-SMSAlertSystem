var createError = require('http-errors');
var express = require('express');
var path = require('path');
const ejs = require("ejs");
var logger = require('morgan');


console.log("-- Routanator 9001 --");
var floodRouter = require('./routes/floodInformation');
var droughtRouter = require('./routes/droughtInformation');
var signupRouter = require('./routes/signup');
var typhoonRouter = require('./routes/typhoonInformation');
var helpRouter = require('./routes/helpGuide');


console.log("---------------------");
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Middleware
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.use('/', floodRouter);
app.use('/', droughtRouter);
app.use('/', signupRouter);
app.use('/', typhoonRouter);
app.use('/', helpRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});

// Error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};
  
    // render the error page
    res.status(err.status || 500);
    res.render('error');
  });
  
  
  module.exports = app;