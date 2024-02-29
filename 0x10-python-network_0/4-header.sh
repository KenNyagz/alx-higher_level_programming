#!/bin/bash
# send GET request
curl -X GET -H "X-School-User-Id: 98" -i "$1" | sed '1,/^$/d'
