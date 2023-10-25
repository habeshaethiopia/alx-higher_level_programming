#!/usr/bin/node
// read the file in js
const fs = require('fs')
const { argv } = require('process')
fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err)
  }
  console.log(data)
})
