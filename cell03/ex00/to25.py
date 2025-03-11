#!/usr/bin/env python3

def main():
    # Accept user input and store it in a numeric variable
    try:
        num = int(input("Enter a number: "))
        
        # Check if the input number is greater than 25
        if num > 25:
            print("Error")
        else:
            # Loop from the input number up to 25 (inclusive)
            for i in range(num, 26):
                print(i)
    except ValueError:
        print("Please enter a valid number.")

# Ensure the program runs when executed
if __name__ == "__main__":
    main()
