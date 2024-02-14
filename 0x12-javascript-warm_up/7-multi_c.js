#!/usr/bin/node
const myInput = process.argv[2];
const myVar = ['C is fun'];
if (isNaN(myInput)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myInput; i++) {
    console.log(myVar[0]);
  }
}
