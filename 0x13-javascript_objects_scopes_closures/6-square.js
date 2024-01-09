#!/usr/bin/node

const Square = require('./5-square.js');

class Square extends Square {

  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
  if (Object.keys(this).length === 0) {
      console.log('');
    } else {
        let chr = c;
        if (c === undefined) {
           c = "X";
        }
        for (let i = 0; i < this.height; i++) {
          console.log(chr.repeat(this.width));
        }
    }
  }
}

module.exports = Square;
