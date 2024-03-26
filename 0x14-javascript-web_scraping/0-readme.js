#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('File content:', data);
  }
});
