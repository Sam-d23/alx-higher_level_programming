#!/usr/bin/node
const dict = require('./101-data').dict;

const New_Dict = {};

for (const [key, val] of Object.entries(dict)) {
  New_Dict[val] ? New_Dict[val].push(key) : (New_Dict[val] = [key]);
}
console.log(New_Dict);
