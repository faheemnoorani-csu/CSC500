# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.

def main():
    # Get user input
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Perform addition
    addition_result = num1 + num2
    print(f"The addition of {num1} and {num2} is: {addition_result}")

    # Perform subtraction
    subtraction_result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is: {subtraction_result}")


if __name__ == "__main__":
    main()