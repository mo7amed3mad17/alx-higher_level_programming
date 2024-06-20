#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const x = Number(process.argv[2]);
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
