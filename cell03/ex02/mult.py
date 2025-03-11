#!/usr/bin/env python3

def main():
    while True:
        # Accept user input
        user_input = input("Say something: ")
        
        # If the user enters "STOP", break out of the loop
        if user_input.strip().upper() == "STOP":
            print("Program stopped.")
            break
        
        # Print a response for each input
        print(f"I got that: {user_input}")
    
if __name__ == "__main__":
    main()
