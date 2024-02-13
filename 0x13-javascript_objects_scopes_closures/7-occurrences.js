#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((cur) => {
    if (cur === searchElement) count++;
  });
  return count;
};
