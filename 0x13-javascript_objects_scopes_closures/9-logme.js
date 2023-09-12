#!/usr/bin/node
let num = 1;
exports.logMe = function (item) {
  console.log(`${num}: ${item}`);
  num++;
};
