#!/usr/bin/node
// Number of films with the given character

const request = require('request');
const urlLink = process.argv[2];
let iter = 0;

request.get(urlLink, function (errorr, okResponse, body) {
  if (errorr) {
    console.log(errorr);
  } else {
    const dataShow = JSON.parse(body);
    dataShow.results.forEach((itemValue) => {
      itemValue.characters.forEach((itemValueChar) => {
        if (itemValueChar.includes(18)) {
          iter += 1;
        }
      });
    });
    console.log(iter);
  }
});
