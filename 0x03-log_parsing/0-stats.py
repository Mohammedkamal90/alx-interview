#!/usr/bin/python3
'''script for parsing HTTP request logs
'''

import sys


def print_statistics(total_file_size, status_code_counts):
    print("File size: {:d}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        if count > 0:
            print("{:d}: {:d}".format(status_code, count))

def run():
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) != 7:
                continue

            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            total_file_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)

if __name__ == "__main__":
    run()
