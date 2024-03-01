#!/usr/bin/python3
'''sends a POST request to a passed URL and email,displays response body
'''
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    reqst = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(reqst) as resp:
        cont = resp.read().decode('utf-8')
        print(body)
