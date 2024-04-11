#!/usr/bin/python3
'''list 10 commits of a repository(github) '''
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    params = {'per_page': 10}
    headers = {'Accept': 'application/vnd.github.v3+json'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            commit_data = commit['commit']
            commit_hash = commit['sha']
            author = commit_data['author']['name']
            print(f'{commit_hash}: {author}')
    else:
        print("error")
