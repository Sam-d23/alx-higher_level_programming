#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arg_int = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[arg_int.length - 2]);
}
