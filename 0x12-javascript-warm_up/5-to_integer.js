#!/usr/bin/node

const args = process.argv.slice(2);

const argSize = Number(args[0]);

if (isNaN(argSize) === false) {
  console.log(`My number: ${argSize}`);
} else {
  console.log('Not a number');
}
