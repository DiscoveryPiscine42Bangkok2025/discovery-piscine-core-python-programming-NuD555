#!/usr/bin/env python3
import sys
import re

def scan_it():
    if len(sys.argv) != 3:
        print("none")
        return
    
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(keyword, text)

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))

if __name__ == "__main__":
    scan_it()