#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const int_args = args.sort((a, b) => a - b);
  console.log(int_args[int_args.length - 2]);
}
