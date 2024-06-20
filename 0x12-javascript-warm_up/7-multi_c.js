#!/usr/bin/node

const arg = process.argv[2];
let i = 0;

if (!parseInt(arg)) {
  console.log('Missing number of occurrences');
} else {
  while (i <= Number(arg)) {
    console.log('C is fun');
    i++;
  }
}
