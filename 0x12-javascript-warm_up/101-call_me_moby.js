#!/usr/bin/node

function executeXTimes(x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
}

module.exports.executeXTimes = executeXTimes;

