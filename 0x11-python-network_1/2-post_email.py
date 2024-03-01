#!/usr/bin/python3
'''sends a POST request to a passed URL and email,displays response body
'''
from urllib import parse, request
import sys


def send_post_request(url, email):
    data = parse.urlencode({'email': email}).encode()
    req = request.Request(url, data=data)  # this will make the method "POST"

    # Send the request and receive the response
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
