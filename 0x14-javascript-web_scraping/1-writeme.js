#!/usr/bin/node
// to WRITE from file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (errorr) {
    if (errorr) {
      console.log(errorr);
    }
  });
