#!/usr/bin/node
const fs = require('fs');

function concatFiles (sourceFile1, sourceFile2, destinationFile) {
  try {
    const content1 = fs.readFileSync(sourceFile1, 'utf8');
    const content2 = fs.readFileSync(sourceFile2, 'utf8');

    const concatenatedContent = content1 + content2;

    fs.writeFileSync(destinationFile, concatenatedContent);
  } catch (error) {}
}
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];
concatFiles(sourceFile1, sourceFile2, destinationFile);
