#!/usr/bin/node

const dict = require('./101-data').dict;
const new_dict = Object.entries(dict).reduce((item, [k, v]) => {
  item[v] = item[v] ? [...item[v], k] : [k];
  return item;
}, {});

console.log(new_dict);
