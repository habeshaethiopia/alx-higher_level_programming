#!/usr/bin/node
// print complited
const request = require('request');

const options = { json: true };
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, options, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    (body.characters)
      .map(x => request(x, options, (error, res, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(body.name);
        }
      }));
  }
}
);
