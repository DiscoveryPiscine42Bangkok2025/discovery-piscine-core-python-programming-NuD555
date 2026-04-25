#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    outer = 0
    while outer <= 10:
        print(f"Table de {outer}:", end="")

        inner = 0
        while inner <= 10:
          
            print(f" {outer * inner}", end="") 
            inner += 1
        
        print() 
        outer += 1