#!/usr/bin/python3
"""
Script taking in URL and an email, sends a POST request to
the passed URL with email as a parameter, and displaying
body of response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        extracted_email = None

        parsed_response = urllib.parse.parse_qs(body)
        if 'email' in parsed_response:
            extracted_email = parsed_response['email'][0]
        print("Your email is: {}".format(extracted_email))
