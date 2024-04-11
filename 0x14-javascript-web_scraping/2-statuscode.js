#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

if (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
} else {
  console.error('Please provide a URL as an argument');
}
