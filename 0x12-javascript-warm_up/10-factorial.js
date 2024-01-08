#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  }
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

const args = process.argv;
const num = parseInt(args[2]);

if (args.length < 3) {
  console.log(1);
}
if (!isNaN(num)) {
  console.log(factorial(num));
}
