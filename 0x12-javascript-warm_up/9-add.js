#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log('NaN');
}
