#!/usr/bin/node
// Number of films with the given character

const request = require('request');
const urlLink = process.argv[2];

request.get(urlLink, { json: true }, function (errorr, okResponse, body) {
  if (errorr) {
    console.log(errorr);
  }
  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
