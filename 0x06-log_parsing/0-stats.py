#!/usr/bin/python3
"""Script to get stats from a request"""

import sys

codes = {}
status = ['200', '301', '400', '401', '403', '404', '405', '500']
i = 0
x = 0

try:
    for ln in sys.stdin:
        if i == 10:
            print(f"File size: {x}")
            for key in sorted(codes):
                print(f"{key}: {codes[key]}")
            i = 1
        else:
            i += 1

        ln = ln.split()

        try:
            x = x + int(ln[-1])
        except (IndexError, ValueError):
            pass

        try:
            if ln[-2] in status:
                if codes.get(ln[-2], -1) == -1:
                    codes[ln[-2]] = 1
                else:
                    codes[ln[-2]] += 1
        except IndexError:
            pass

    print("File size: {}".format(x))
    for key in sorted(codes):
        print(f"{key}: {codes[key]}")

except KeyboardInterrupt:
    print("File size: {}".format(x))
    for key in sorted(codes):
        print(f"{key}: {codes[key]}")
    raise
