#!/bin/bash
# Sending a JSON POST request to the URL passed as the first argument, and displays the body of the response.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
