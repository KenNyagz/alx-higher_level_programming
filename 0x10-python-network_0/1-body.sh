#!/bin/bash
# Send GET req to URL, display body of Response
response=$(curl -s -o /dev/stdout -w "%{http_code}" "$1" | grep -Pzo "(?s)(?<=HTTP/1\.[01] 200 OK).*?(?<=\r?\n\r?\n)" | tr -d '\0'); [[ "$(tail -n1 <<<"$response")" == "200" ]] && head -n-1 <<<"$response" || echo ""
