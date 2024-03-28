#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print("Your GitHub id is:", data['id'])
    else:
        print("Failed to retrieve GitHub id. Status code:", response.status_code)

