#!/bin/bash
# Sending a request to the URL passed as an argument, and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
