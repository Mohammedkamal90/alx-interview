#!/usr/bin/python3


import sys
from collections import defaultdict


def print_stats(total_size, status_counts):
    """method print
    return
    nothing
    """
    print("File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def parse_line(line):
    parts = line.split()
    if len(parts) != 10:
        return None
    ip, date, method, path, protocol, status, size = parts[:7]
    if method != 'GET' or path != '/projects/260' or protocol != 'HTTP/1.1':
        return None
    try:
        size = int(size)
        status = int(status)
    except ValueError:
        return None
    return status, size

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0
    try:
        for line in sys.stdin:
            parsed = parse_line(line.strip())
            if parsed:
                status, size = parsed
                total_size += size
                status_counts[status] += 1
                line_count += 1
            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0
    except KeyboardInterrupt:
        pass
    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
