#!/usr/bin/node
// to WRITE from file

const request = require('request');
const urlLink = process.argv[2];

request.get(urlLink, function (errorr, okResponse) {
  if (errorr) {
    console.log(errorr);
  } else {
    console.log('code: ' + okResponse.statusCode);
  }
});
