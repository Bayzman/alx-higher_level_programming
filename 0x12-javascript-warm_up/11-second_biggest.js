#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const argSorted = args.map((arg) => Number(arg)).sort((a, b) => b - a);
  console.log(argSorted[1]);
}
