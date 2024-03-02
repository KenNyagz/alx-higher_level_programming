#!/usr/bin/python3
'''list 10 commits of a repository(github) '''
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://github.com/{owner}/{repo}/commits"

    params = {'per_page': 10}
    response = requests.get(url, params=params)
    print(response.json())

    if response.status_code == 200:
        commits = response.json()
        print(commits)
        for commit in commits:
            commit_hash = commit['commit']
            author = commit_hash['author']['name']
            print(f'{commit_hash}: {author}')
    else:
        print("error")
