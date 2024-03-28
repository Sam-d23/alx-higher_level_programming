#!/usr/bin/node

const fs = require('fs');
const http = require('http');

const url = process.argv[2];
const filePath = process.argv[3];

http.get(url, (response) => {
  let data = '';

  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    fs.writeFile(filePath, data, (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Successfully saved data to ${filePath}`);
      }
    });
  });
}).on('error', (err) => {
  console.error(`Error retrieving data from ${url}: ${err.message}`);
});
