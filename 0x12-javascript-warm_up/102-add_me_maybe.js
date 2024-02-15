#!/usr/bin/node
exports.addMe = function (num, theFunction) {
  theFunction(++num);
};
