#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      const template = [];
      for (let j = 0; j < this.width; j++) template.push('X');
      console.log(`${template.join('')}`);
    }
  }
}

module.exports = Rectangle;
