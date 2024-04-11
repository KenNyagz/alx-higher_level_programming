#!/usr/bin/node

const cmdArgs = process.argv;

const firstArg = parseInt(cmdArgs[2]);

if (!isNaN(firstArg)) {
  console.log('My number:', firstArg);
} else {
  console.log('Not a number');
}
