#!/usr/bin/node
const args = process.argv;
const le = args.length;
if (le === 2) {
  console.log('No argument');
} else if (le === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
