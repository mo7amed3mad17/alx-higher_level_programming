#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const arg = Number.parseInt(process.argv[2]);
  if (isNaN(arg)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + arg);
  }
}
