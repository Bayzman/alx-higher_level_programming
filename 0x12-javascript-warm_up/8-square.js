#!/usr/bin/node

const args = process.argv.slice(2);

const argSize = Number(args[0]);

if (isNaN(argSize) === false) {
  for (let i = 0; i < numArg; i++) {
    console.log('X'.repeat(numArg));
  }
} else {
  console.log('Missing size');
}
