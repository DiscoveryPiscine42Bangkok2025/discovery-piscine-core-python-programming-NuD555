#!/usr/bin/env python3
import sys

def aff_rev_params(): 
    params = sys.argv[1:]

    if len(params) < 2:
        print("none")
    else:
        for item in reversed(params):
            print(item)

if __name__ == "__main__":
    aff_rev_params()
