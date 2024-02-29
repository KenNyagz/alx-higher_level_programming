#!/bin/bash
# Send GET req to URL, display body of Response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1");[ "$response" == "200" ] && curl -s "$1" 
