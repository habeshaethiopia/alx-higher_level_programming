#!/usr/bin/node
// printing the status code
const request = require('request');
const { argv } = require('process');
const url = `${argv[2]}`;

const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const films = body.results;
  console.log(films.reduce((c, e) => {
    e.characters.forEach(el => el.includes('18') ? c++ : c);
    return c;
  }, 0));
});
