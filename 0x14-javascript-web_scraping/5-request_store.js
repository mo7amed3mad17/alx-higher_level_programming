#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const store = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  fs.writeFile(store, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
