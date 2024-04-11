#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response
while handling http errors'''
from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            body = resp.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code:", e.code)
