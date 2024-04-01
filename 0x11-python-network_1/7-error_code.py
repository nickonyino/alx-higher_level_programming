#!/usr/bin/python3
"""
 script takes in a URL, sends a request to  URL and
displaying the body of response If  HTTP status code => 400
print: Error code: followed by the value of the
HTTP status code
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(response.text)

