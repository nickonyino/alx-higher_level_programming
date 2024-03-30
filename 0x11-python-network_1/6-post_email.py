#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to
passed URL with email as a parameter, and displaying the
body of response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is: {}".format(response.text.strip()))
