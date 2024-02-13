#!/usr/bin/node
const { argv } = require('process');
let l = 0;

argv.forEach(() => l++);

console.log(l === 2 ? 'No argument' : argv[2]);
