#!/usr/bin/python3
'''sends a POST request to a passed URL and email,displays response body
'''
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    parameter = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(parameter)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode("ascii"))
