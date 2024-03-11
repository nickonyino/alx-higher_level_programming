#!/usr/bin/node

const  argsnumber = process.argv.length;

if (argsnumber === 2)
{
	console.log("No argument");
}
else if (argsnumber === 3)
{
	console.log("Argument found");
}
else 
{
	console.log("Arguments found");
}

