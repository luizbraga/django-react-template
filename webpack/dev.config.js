var config = require('./base.config.js');
var path = require('path');
var webpack = require('webpack');

config.output = {
  path: path.join(__dirname, '../static/builds-dev/'),
  filename: '[name]-[hash].js',
  publicPath: 'http://0.0.0.0:3000/static/builds/'
}

module.exports = config;
