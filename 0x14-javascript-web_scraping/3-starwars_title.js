#!/usr/bin/node
// printing the status code
const request = require('request');
const { argv } = require('process');
const url = argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
