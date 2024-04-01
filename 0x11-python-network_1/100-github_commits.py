#!/usr/bin/python3
"""
Module to access the GitHub API and list recent commits
"""
import requests
from sys import argv

def print_commits(commit_list):
    """
    Print the commit SHA and author name for each commit in the list
    """
    for commit in commit_list:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

def main(argv):
    """
    Main function to list recent commits of a repository
    """
    if len(argv) != 3:
        print("Usage: ./script.py [repository] [owner]")
        return

    repo = argv[1]
    owner = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}

    # Send request to GitHub API to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commit_list = response.json()
        print_commits(commit_list[:10])  # Print the 10 most recent commits
    else:
        print("Failed to fetch commits:", response.status_code)

if __name__ == "__main__":
    main(argv)

