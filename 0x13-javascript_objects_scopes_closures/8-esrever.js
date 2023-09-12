#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let f = 0;
  while ((len - f) > 0) {
    const aux = list[len];
    list[len] = list[f];
    list[f] = aux;
    f++;
    len--;
  }
  return list;
};
