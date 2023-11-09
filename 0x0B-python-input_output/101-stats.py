#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys


def print_metrics(sc, fs):


    print(f"File size: {fs}")
    for code in sorted(sc.keys()):
        print(f"{code}: {sc[code]}")

def parse_log_line(line, sc, fs):
    elements = line.strip().split(" ")
    if len(elements) == 9:
        code = elements[7]
        file_size = int(elements[8])
        fs += file_size
        if code in sc:
            sc[code] += 1
        else:
            sc[code] = 1
    return sc, fs

def main():
    sc = {}
    fs = 0
    lc = 0

    try:
        for line in sys.stdin:
            sc, fs = parse_log_line(line, sc, fs)
            lc += 1

            if lc % 10 == 0:
                print_metrics(sc, fs)

    except KeyboardInterrupt:
        pass

    print_metrics(sc, fs)


if __name__ == "__main__":
    main()
