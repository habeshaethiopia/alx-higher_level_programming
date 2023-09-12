#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (const i in Range(this.height)) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
