var config = require('./base.config.js');
var path = require('path');
var webpack = require('webpack');

config.output = {
  path: path.join(__dirname, '../static/builds/'),
  filename: '[name]-[hash].js',
  publicPath: '/static/builds/'
}

module.exports = config;
