#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dic = {};
for (const key in dict) {
  if (dict[key] in dic) {
    dic[dict[key]].push(key);
  } else {
    dic[dict[key]] = [key];
  }
}
console.log(dic);
