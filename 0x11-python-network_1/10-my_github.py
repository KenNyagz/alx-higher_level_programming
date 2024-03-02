#!/usr/bin/python3
''' takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = 'https://api.github.com/user'

    # auth = (username, passwd)
    #headers = {'Accept': "application/vnd.github.v3+json"}
    headers = {'Authorization': f'Basic {username}:{passwd}'}

    #response = requests.post(url, auth=auth)
    response = requests.get(url, headers=headers)

    user_data = response.json()
    print(user_data['id']) #user id
    #if response.status_code == 200:
        #user_info = response.json()  # Parse the response JSON
        #print(user_info['id'])
    #else:
        #print('None')
