#!/usr/bin/node
// stotre the response in file
const fs = require('fs');
const { argv } = require('process');
const request = require('request');
const url = `${argv[2]}`;

const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }

  if (!error && res.statusCode === 200) {
    fs.writeFile(argv[3], body, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
