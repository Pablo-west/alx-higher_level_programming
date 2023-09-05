#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:d}{:d}, ".format(tens_digit, ones_digit), end="")

print("{:d}{:d}".format(9, 9))
