#!/usr/bin/node

const cmdArgs = process.argv;

if (cmdArgs[2] === undefined){
  cmdArgs[2] = "undefined";
}
if (cmdArgs[3] === undefined){
  cmdArgs[3] = "undefined";
} 
console.log(cmdArgs[2] + " is " + cmdArgs[3]);
