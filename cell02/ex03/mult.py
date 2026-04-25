#!/usr/bin/env python3

first_str = input("Enter the first number:\n")
first_num = int(first_str)

second_str = input("Enter the second number:\n")
second_num = int(second_str)

result = first_num * second_num

print(f"{first_num} x {second_num} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")