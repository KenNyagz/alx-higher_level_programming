#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error(`Error: File '${err.path}' not found.`);
    } else {
      console.error('Error:', err);
    }
    return;
  }
  console.log('File content:', data);
});
