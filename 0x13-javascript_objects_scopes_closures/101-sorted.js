#!/usr/bin/node

// Import the original dictionary from 101-data.js
const dict = require('./101-data').dict;

// Initialize the new dictionary
const newDict = {};

// Iterate over each entry in the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the occurrence is not yet a key in the new dictionary, add it
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  // Append the user id to the list for the corresponding occurrence
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
