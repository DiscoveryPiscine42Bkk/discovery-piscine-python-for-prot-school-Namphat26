#!/usr/bin/env python3

# Prompt the user to enter a number
number = float(input("Please enter a number: "))

# Check if the number is negative, positive, or zero
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
