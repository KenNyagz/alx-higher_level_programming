#!/bin/bash
# send POST req to url, disp response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
