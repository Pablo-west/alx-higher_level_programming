#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if char_code not in (ord('q'), ord('e')):
        print("{}".format(chr(char_code)), end="")
print("")
