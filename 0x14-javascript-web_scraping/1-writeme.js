#!/usr/bin/node
const fs = require('fs');

function writeFile(filePath, content) {
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error('An error occurred while writing to the file:', err);
        } else {
            console.log('Content has been successfully written to the file.');
        }
    });
}

if (process.argv.length !== 4) {
    console.error('Usage: node script.js <file_path> <content>');
    process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];
writeFile(filePath, content);
