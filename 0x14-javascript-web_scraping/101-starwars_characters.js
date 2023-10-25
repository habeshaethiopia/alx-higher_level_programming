#!/usr/bin/node
// print complited
const request = require('request');

const options = { json: true };
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, options, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = body.characters;
    order(characters, 0);
  }
}
);
function order (characters, i) {
  if (characters.length === i) { return; }
  request(characters[i], (error, res, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(body.name);
      order(characters, i + 1);
    }
  });
}
