#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    bytes_read = response.read()

print("Body response:")
print("\t- type:", type(bytes_read))
print("\t- content:", bytes_read)
print("\t- utf8 content: OK")
