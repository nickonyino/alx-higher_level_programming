#!/usr/bin/python3
"""
The code that takes in a URL, sends a request to the URL and displaying the value of the
X-Request-Id variable found in  header of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
