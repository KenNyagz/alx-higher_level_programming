#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys


def printstats(stats):
    """  """
    totalsize = sum(stats.values())
    print("Total file size: File size: {}".format(totalsize))
    for statuscode in sorted(stats):
        count = stats[statuscode]
        print("{}: {}".format(status_code, count))

def process_input():
    stats = {}
    linecount = 0

    try:
        for line in sys.stdin:
            linecount += 1
            ip, _, _, _, statuscode, filesize = line.split()[0:6]

            if statuscode in status:
                stats[statuscode] += 1
            else:
                stats[statuscode] = 1

            if linecount % 10 == 0:
                printstats(stats)
                print()
    except KeyboardInterrupt:
        printstats(stats)

process_input()
