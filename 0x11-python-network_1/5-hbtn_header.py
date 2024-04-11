#!/usr/bin/python3
'''Sends a request to a URL, displays X-Request-Id in the response header'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    resp_id = resp.headers.get("X-Request-Id")
    print(resp_id)
