#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    // If 'c' is undefined or null, default to 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the specified character 'c'
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
