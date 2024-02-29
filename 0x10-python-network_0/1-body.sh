#!/bin/bash
# Send GET req to URL, display body of Response
curl -s -o response_body.txt -D headers.txt $1 && grep -q "^HTTP.* 200" headers.txt && cat response_body.txt && rm response_body.txt headers.txt
