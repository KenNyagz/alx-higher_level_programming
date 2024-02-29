#!/bin/bash
# Display status code of http URL request
curl -s -o /dev/null -w "%{http_code}" "$1"
