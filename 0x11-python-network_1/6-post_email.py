#!/usr/bin/python3
'''Sends POST request to URL provided URL with an email address as the data
to be added fed to the server and dispalys body'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data)

    print(response.text)
