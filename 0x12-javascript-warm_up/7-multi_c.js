#!/usr/bin/node

const args = process.argv.slice(2);

const arg = Number(args[0]);

if (isNaN(arg) === false) {
  for (let j = 0; j < arg; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
