#!/usr/bin/python3
'''takes in a letter and sends a POST reqst to http://0.0.0.0:5000/search_user
with the letter as a parameter.'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    response = requests.post(url, data=data)

    # Check if response JSON body is a proper JSON
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
