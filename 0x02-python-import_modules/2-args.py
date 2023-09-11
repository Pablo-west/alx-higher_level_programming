#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)

    print("{} argument{}:".format(count, 's' if count != 1 else ''), end="")

    if count == 0:
        print(".")
    else:
        print()
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i]))
