#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url=$1
filename=$2

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' does not exist."
    exit 1
fi

# Send a POST request with the file content as the body
curl -sX POST -H "Content-Type: application/json" --data-binary "@$filename" "$url"

