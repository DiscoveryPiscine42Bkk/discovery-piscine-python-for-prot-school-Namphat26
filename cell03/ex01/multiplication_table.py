#!/usr/bin/env python3

def main():
    # Accept user input and store it in a numeric variable
    try:
        num = int(input("Enter a number to display its multiplication table: "))
        
        # Display the multiplication table for the input number
        print(f"Multiplication table for {num}:\n")
        for i in range(1, 11):  # Loop through numbers 1 to 10
            print(f"{num} x {i} = {num * i}")
    
    except ValueError:
        print("Please enter a valid number.")

# Ensure the program runs when executed
if __name__ == "__main__":
    main()
