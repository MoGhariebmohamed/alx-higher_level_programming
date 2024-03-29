#!/usr/bin/node
// to WRITE from file

const request = require('request');
const urlLink = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(urlLink, function (errorr, okResponse, body) {
  if (errorr) {
    console.log(errorr);
  } else {
    const dataShow = JSON.parse(body);
    const charchter = dataShow.charchters
    for (const charchter of charchters) {
      request.get(charchter, function (error, response, body) {
        if (errorr) {
          console.log(errorr);
	} else {
	  const title = JSON.parse(body);
          console.log(title.name);
        }
      });
    };
  }
});
