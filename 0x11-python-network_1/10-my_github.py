#!/usr/bin/python3
''' takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, passwd))

    if response.status_code == 200:
        user_info = response.json()  # Parse the response JSON
        print(user_info['id'])
    else:
        print("None")
