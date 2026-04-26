#!/usr/bin/env python3
import sys

def parameter_matching():
    if len (sys.argv) != 2:
        print("none")
        return
    original_param = sys.argv[1]

    user_answer = input("What was the parameter? ")

    if user_answer == original_param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    parameter_matching()