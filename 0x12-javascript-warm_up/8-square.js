#!/usr/bin/node

const cmdargs = process.argv;

const size = parseInt(cmdargs[2]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
