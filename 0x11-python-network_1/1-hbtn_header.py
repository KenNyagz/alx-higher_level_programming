#!/usr/bin/python3
'''send request to url and display value of the 'X-Request-Id' variable
obtained from the response header'''
import urllib.request
import sys

url = sys.argv[1]

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
