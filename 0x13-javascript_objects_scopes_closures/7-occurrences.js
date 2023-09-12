#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  let se;
  for (se in list) {
    if (list[se] === searchElement) {
      n++;
    }
  }
  return n;
};
