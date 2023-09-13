#!/usr/bin/node
const arg = process.argv;
function factorial (a = 0) {
  if (!a) { return 1; } else { return a * factorial(a - 1); }
}
const a = parseInt(arg[2]);
console.log(factorial(a));
