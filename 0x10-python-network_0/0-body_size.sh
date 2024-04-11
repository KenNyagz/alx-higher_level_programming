#!/bin/bash
# sends request to a specified url and displays the size of the body
response=$(curl -s -o /dev/null -w "%{size_download}" "$1");echo $response
