#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let d = 0; d < list.length; d++) {
    if (searchElement === list[d]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
