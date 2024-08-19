#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line argument
const starWarsapi = process.argv[2];

// Make a request to the Star Wars API
request(starWarsapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    return;
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body).results;

  // Count the Appearance
  const counter = movie.filter(movie => movie.characters.some(character => character.includes('/people/18/'))).length;
  console.log(counter);
});
