#!/bin/bash
# Get comtent-lenght of a giving IP Address
curl -sI "$1" | awk '/Content-Length/{print $2}'
