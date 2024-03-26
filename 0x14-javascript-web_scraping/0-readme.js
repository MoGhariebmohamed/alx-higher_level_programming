#!/usr/bin/node
//to read from file

const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8',
  function (errorr, req_data) {
    if (errorr) {
      console.log(errorr);
      return;
    }
    console.log(req_data);
  });
