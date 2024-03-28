#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred while making the request:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch webpage. Status code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log('Webpage content saved to', filePath);
      }
    });
  }
});
