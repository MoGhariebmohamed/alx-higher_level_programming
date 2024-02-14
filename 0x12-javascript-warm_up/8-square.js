#!/usr/bin/node
const myInput = process.argv[2];
if (isNaN(myInput)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myInput; i++) {
    let line = '';
    for (let x = 0; x < myInput; x++) {
      line += 'X';
    }
    console.log(line);
  }
}
