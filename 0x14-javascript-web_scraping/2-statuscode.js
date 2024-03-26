#!/usr/bin/n//to read from file
//to WRITE from file

const files = require('files');

files.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (errorr) {
    if (errorr) {
      console.log(errorr);
    }
  });
