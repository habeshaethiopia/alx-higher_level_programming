#!/usr/bin/node
const arg = process.argv;
if (!arg[3]) console.log(0);
else {
  const newarr = [];
  for (let i = 2; i < arg.length; i++) {
    const x = parseInt(arg[i]);
    if (x) { newarr.push(x); }
  }
  newarr.sort((a, b) => a - b);
  console.log(newarr);
  console.log(newarr[newarr.length - 2]);
}
