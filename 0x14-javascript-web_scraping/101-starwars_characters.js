#!/usr/bin/node
// print complited
const request = require('request');
const { argv } = require('process');
const url = `${argv[2]}`;
const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body.reduce((acc, cur) => {
      if (cur.completed) {
        if (acc[cur.userId]) {
          acc[cur.userId]++;
        } else {
          acc[cur.userId] = 1;
        }
      }
      return acc;
    }, {}));
  }
}
);
