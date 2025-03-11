num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

print(f"The result of {num1} + {num2} is: {addition}")
print(f"The result of {num1} - {num2} is: {subtraction}")
print(f"The result of {num1} * {num2} is: {multiplication}")
print(f"The result of {num1} / {num2} is: {division}")
