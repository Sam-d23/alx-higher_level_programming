#!/usr/bin/node

const { argv } = require('process');
const arg = parseInt(argv[2]);

console.log(Number.isInteger(arg) ? `My number: ${arg}` : 'Not a number');
