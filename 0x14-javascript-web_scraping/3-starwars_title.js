#!/usr/bin/node
// to WRITE from file

const request = require('request');
const urlLink = 'https://swapi-api.alx-tools.com/api/films' + process.argv[2];

request.get(urlLink, (errorr, okResponse, content) => {
  if (errorr) {
    console.log(errorr);	
  } else {
      const finalData = JSON.parse(content);
      console.log(finalData.title);
  }
});
