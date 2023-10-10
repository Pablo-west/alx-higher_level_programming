#!/usr/bin/python3

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_metrics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
    except ValueError:
        pass

    # Print metrics every 10 lines
    if len(status_code_counts) % 10 == 0:
        print_metrics()
