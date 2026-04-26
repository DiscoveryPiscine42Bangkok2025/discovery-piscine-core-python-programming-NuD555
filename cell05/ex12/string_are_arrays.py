#!/usr/bin/env python3
import sys

def string_are_arrays():
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]
    result = ""

    for char in text:
        if char == 'z':
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    string_are_arrays()