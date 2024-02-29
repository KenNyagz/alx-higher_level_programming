#!/bin/bash
# display all HTTP methods the server will accept
curl -s OPTIONS "$1"
