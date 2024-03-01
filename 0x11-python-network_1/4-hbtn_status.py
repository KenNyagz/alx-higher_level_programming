#!/usr/bin/python3
'''Sends request to url, displays response body'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response = response.content.decode('utf-8')

    print("Body Response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
