#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const toAppend = process.argv[3];

fs.writeFile(path, toAppend, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
}
);
