#!/usr/bin/node

const args = process.argv.slice(2);

const myVar = `${args[0]} is ${args[1]}`;

console.log(myVar);
