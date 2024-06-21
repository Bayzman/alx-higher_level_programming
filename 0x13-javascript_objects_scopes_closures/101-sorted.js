#!/usr/bin/node

const dict = require('./101-data.js').dict;

const userByOccurrences = {};

for (const id in dict) {
  const occurrences = dict[id];

  if (!userByOccurrences[occurrences]) {
    userByOccurrences[occurrences] = [];
  }

  userByOccurrences[occurrences].push(id);
}

console.log(userByOccurrences);
