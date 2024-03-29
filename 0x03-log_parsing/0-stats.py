#!/usr/bin/python3
'''script for parsing HTTP request logs
'''

import sys

STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

def process_line(line):
    line_list = line.split(" ")
    if len(line_list) >= 10:
        code = line_list[-2]
        size = int(line_list[-1])
        if code in STATUS_CODES:
            return code, size
    return None, 0

def print_statistics(total_size, code_counts):
    print('File size:', total_size)
    for code in sorted(STATUS_CODES):
        if code_counts[code] != 0:
            print(f'{code}: {code_counts[code]}')

def main():
    total_size = 0
    code_counts = {code: 0 for code in STATUS_CODES}
    try:
        for i, line in enumerate(sys.stdin, start=1):
            code, size = process_line(line)
            if code:
                total_size += size
                code_counts[code] += 1
            if i % 10 == 0:
                print_statistics(total_size, code_counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(total_size, code_counts)

if __name__ == "__main__":
    main()
