#!/usr/bin/python3
'''sends a POST request to a passed URL and email,displays response body
'''
from urllib import parse, request
import sys

def send_post_request(url, email):
    # Prepare the data to be sent in the POST request
    data = parse.urlencode({'email': email}).encode()
    
    # Create a request object
    req = request.Request(url, data=data) # this will make the method "POST"
    
    # Send the request and receive the response
    with request.urlopen(req) as response:
        # Read the response body and decode it
        response_body = response.read().decode('utf-8')
        print(response_body)

if __name__ == "__main__":
    # Extract the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Call the function to send the POST request
    send_post_request(url, email)
