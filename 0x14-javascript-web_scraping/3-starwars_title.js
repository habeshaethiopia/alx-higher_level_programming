#!/usr/bin/node
// printing the status code
const request = require('request');
const { argv } = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
let result;
const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }

  if (!error && res.statusCode === 200) {
    console.log(body.title);
  }
});
