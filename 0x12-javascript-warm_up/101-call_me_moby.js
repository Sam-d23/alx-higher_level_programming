#!/usr/bin/node

exports.add = function (x, theFunction) {
  theFunction(++x);
};
