#!/usr/bin/env python3

def print_multiplication_table():
    for num in range(1, 11):  # Loop through numbers 1 to 10
        print(f"Multiplication Table for {num}:")
        for i in range(1, 11):  # Loop through numbers 1 to 10 for multiplication
            print(f"{num} x {i} = {num * i}")
        print()  # Blank line between each table for readability

def main():
    print_multiplication_table()

if __name__ == "__main__":
    main()
