#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (newDict[occurrences]) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
}

console.log(newDict);
