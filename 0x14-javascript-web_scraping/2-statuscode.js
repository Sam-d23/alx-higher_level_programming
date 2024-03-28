#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else {
    console.log(`Status code: ${response.statusCode}`);
  }
});
