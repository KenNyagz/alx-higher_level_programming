#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
prints the metrics
"""

import sys
import signal

metrics = {
           'totalsize': 0,
           'status_code': {200: 0, 301: 0, 400: 0, 401: 0,
                           403: 0, 404: 0, 405: 0, 500: 0}
          }

def print_metrics():
    """prints the stats using a specified format"""
    print(f"Total file size: {metrics['totalsize']}")
    for code, count in sorted(metrics['status_code'].items()):
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    """Not sure tbh"""
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    linecount = 0
    for line in sys.stdin:
        linecount += 1
        parts = line.split()
        filesize = int(parts[-1])
        status_code = int(parts[-2])

        metrics['totalsize'] += filesize
        if status_code in metrics['status_code']:
            netrics['status_code'][status_code] += 1

        if linecount % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
