#!/usr/bin/node

const args = process.argv.slice(2);

const argSize = Number(args[0]);

if (isNaN(argSize) === false) {
  for (let i = 0; i < argSize; i++) {
    console.log('X'.repeat(argSize));
  }
} else {
  console.log('Missing size');
}
