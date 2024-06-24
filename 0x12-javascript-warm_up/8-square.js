#!/usr/bin/node

const args = Number(process.argv[2]);
const sqrChar = 'X';

if (args) {
  for (let i = 0; i < args; i++) {
    console.log(sqrChar.repeat(args));
  }
} else {
  console.log('Missing size');
}
