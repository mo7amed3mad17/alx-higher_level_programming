#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined || isNaN(arg)) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
