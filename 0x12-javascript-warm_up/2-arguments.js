#!/usr/bin/node
const args = process.argv;
const le = args.length;
if (le === 1) {
  console.log('no argument');
} else if (le === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
