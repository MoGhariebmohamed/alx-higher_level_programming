#!/usr/bin/node
// to WRITE from file

const request = require('request');
const url_link = process.argv[2];

getit.get(url_link,  function (errorr, ok_response) {
    if (errorr) {
      console.log(errorr);
    } else {
	    console.log("code: " + ok_response.statusCode)
  }
});
