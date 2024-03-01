#!/usr/bin/python3
"""
 Python script that takes 2 arguments that lists 10 commits
 (from the most recent to oldest) of a github repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    re = requests.get(url)
    commits = re.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
