#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    rlist[j] = list[i];
  }
  return rlist;
};
