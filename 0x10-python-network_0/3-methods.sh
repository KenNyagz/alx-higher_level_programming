#!/bin/bash
# display all HTTP methods the server will accept
curl -s OPTIONS -i "$1" | grep "Allow:" | cut -d' ' -f2-
