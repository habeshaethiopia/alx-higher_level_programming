#!/usr/bin/node
const arg = process.argv;
if (!arg[3]) console.log(0);
else {
  const newarr = [];
  for (let i = 2; i < arg.length; i++) {
    newarr.push(parseInt(arg[i]));
  }
  newarr.sort();
  console.log(newarr[newarr.length - 2]);
}
