#!/usr/bin/node
const fs = require('fs');

function readFile(filePath) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('An error occurred while reading the file:', err);
        } else {
            console.log(data);
        }
    });
}

if (process.argv.length !== 3) {
    console.error('Usage: node script.js <file_path>');
    process.exit(1);
}

const filePath = process.argv[2];
readFile(filePath);
