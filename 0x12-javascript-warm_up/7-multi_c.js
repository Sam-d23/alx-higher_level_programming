#!/usr/bin/node

const { argv } = require('process');
const x = parseInt(argv[2]);
const msg = (cout) => {
  for (; cout > 0; cout--) console.log('C is fun');
};

Number.isInteger(x) ? printC(x) : console.log('Missing number of occurrences');
