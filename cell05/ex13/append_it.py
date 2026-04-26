#!/usr/bin/env python3
import sys 

def append_it():
    params = sys.argv[1:]
   
    if not params:
        print("none")
        return
    
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")

if __name__ == "__main__":
    append_it()





