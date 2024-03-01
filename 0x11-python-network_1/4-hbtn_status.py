#!/usr/bin/python3
'''Sends request to url, displays response body'''
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print("Body Response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
