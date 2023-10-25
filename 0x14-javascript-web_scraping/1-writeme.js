#!/usr/bin/node
// write the file in js
const fs = require('fs')
const { argv } = require('process')
fs.writeFile(argv[2], argv[3])
