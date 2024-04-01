#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response. If the HTTP status code is greater
than or equal to 400, it prints: Error code: followed by the value of
the HTTP status code
"""
import requests
from sys import argv


def main(argv):
    """
    Method that manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)
