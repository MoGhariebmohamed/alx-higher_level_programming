#!/usr/bin/node
function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];
  const sum = Number(a) + Number(b);
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(sum);
  }
}add();
