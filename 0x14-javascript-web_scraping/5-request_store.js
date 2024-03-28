#!/usr/bin/node
// Number of films with the given character

const request = require('request');
const fs = require('fs');
const urlLink = process.argv[2];

request.get(urlLink, function (errorr, okResponse, body) {
  if (errorr) {
    console.log(errorr);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
