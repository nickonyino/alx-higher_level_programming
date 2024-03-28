#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a URL parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Encode the data to bytes

    # Send a POST request to the URL with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')

        # Display the body of the response
        print(body)

