#!/usr/bin/node
const args = process.argv;
if (!args[2] || !parseInt(args[2])) { console.log('Missing number of occurrences'); } else {
  for (let i = 0; i < parseInt(args[2]); i++) { console.log('C is fun'); }
}
