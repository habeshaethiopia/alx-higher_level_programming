#!/usr/bin/node
const args = process.argv;
const conv = parseInt(args[2]);
if (conv && args[2]) {
  console.log(`My number: ${conv}`);
} else {
  console.log('Not a number');
}
