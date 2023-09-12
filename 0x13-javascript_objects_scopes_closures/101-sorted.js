#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const t in valsUniq) {
  const list = [];
  for (const v in totalist) {
    if (totalist[v][1] === valsUniq[t]) {
      list.unshift(totalist[v][0]);
    }
  }
  newDict[valsUniq[t]] = list;
}
console.log(newDict);
