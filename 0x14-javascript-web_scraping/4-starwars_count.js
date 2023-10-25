#!/usr/bin/node
// printing the status code
const request = require('request');
const { argv } = require('process');
const url = (`${argv[2]}`).replace('films', 'people/18');

const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }

  if (!error && res.statusCode === 200) {
    console.log(body.films.length);
  }
});
