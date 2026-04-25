#!/usr/bin/env python3

val = input()

number = int(val)

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")