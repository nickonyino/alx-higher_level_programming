#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id header from the response
        x_request_id = response.headers.get('X-Request-Id')

        # Display the value of the X-Request-Id variable
        print(x_request_id)
