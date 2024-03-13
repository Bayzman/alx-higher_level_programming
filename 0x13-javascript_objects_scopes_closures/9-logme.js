#!/usr/bin/env node

let argsNum = 0;

exports.logMe = function (item) {
  console.log(`${argsNum}: ${item}`);
  argsNum++;
};
