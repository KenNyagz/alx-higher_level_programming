#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  const numbers = args.slice(2).map(Number);

  if (numbers.length < 2) {
    console.log(0);
  } else {
    const sortedNums = numbers.sort((a, b) => b - a);
    const secondbiggest = sortedNums[1];
    console.log(secondbiggest);
  }
}
