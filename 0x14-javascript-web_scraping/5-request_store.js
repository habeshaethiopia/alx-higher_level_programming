#!/usr/bin/node
// stotre the response in file
const fs = require('fs');
const { argv } = require('process');
const request = require('request');
const url = `${argv[2]}`;

const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    if (body) {
      fs.writeFile(argv[3], body, 'utf8', err => {
        if (err) {
          console.log(err);
        }
      });
    } else {
      fs.writeFile(argv[3], '', 'utf8', err => {
        if (err) {
          console.log(err);
        }
      });
    }
  }
}
);
