import express from 'express';

var express = require('express');
var path = require('path');

var app = express();
const isProduction = process.env.NODE_ENV === 'production';

var port = isProduction ? process.env.PORT : 3000;
var publicPath = path.resolve(__dirname, 'public');


if (!isProduction) {
  let webpack = require('webpack');
  let webpackMiddleware = require('webpack-dev-middleware');
  let webpackHotMiddleware = require('webpack-hot-middleware');
  let config = require('./config.dev.js');
  // serve the content using webpack
  app.use(middleware);
  app.use(webpackHotMiddleware(compiler));
} else {
  // serve the content using static directory
  // app.use(express.static(staticPath));  // Use nginx to serve static files
  app.use(express.static(publicPath));
}

app.listen(port, function () {
  console.log('Server running on port ' + port);
});
