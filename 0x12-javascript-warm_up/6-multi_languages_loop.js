#!/usr/bin/node
const input1 = process.argv[2];
if (isNaN(input1)) {
  console.log('Not a number');
} else {
  console.log('My number: ', Number(input1));
}
