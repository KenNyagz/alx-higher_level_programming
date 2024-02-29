#!/bin/bash
# Send GET req to URL, display body of Response
curl -s -o response.txt -w "%{http_code}" $1 | grep -q "^200 OK$" && cat response.txt && rm response.txt
