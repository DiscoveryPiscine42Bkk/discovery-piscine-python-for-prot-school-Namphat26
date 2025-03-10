#!/usr/bin/env python3

# Pre-defined password
password = "1234"

# Prompt the user to enter the password
entered_password = input("Please enter the password: ")

# Check if the entered password matches the pre-defined password
if entered_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
