#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);
const character = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(character.repeat(num));
  }
}
