#!/usr/bin/node
const input1 = process.argv[2];
if (typeof input1 === Number) {
  console.log('My number: ', Number(input1));
} else {
  console.log('Not a number');
}
