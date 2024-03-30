#!/usr/bin/python3
"""
A Python script that takes 2 arguments in to solve this challenge.
First argument will be the repository name
second argument will be the ow
Don’t need arguement as(number or type)
"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(owner_name, repo_name)
    response = requests.get(url)
    commits_list = response.json()
    for i in range(10):
        print("{}: {}".format(commits_list[i].get('sha'), commits_list[i].
              get('commit').get('author').get('name'))))
