#!/usr/bin/python3
'''Sends request to url, displays response body'''
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
body = response.content.decode('utf-8')

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body)
