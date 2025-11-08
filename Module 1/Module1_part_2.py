# Part 2:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

def main():
    # Get user input
    num1 = float(input("Type the first number (num1): "))
    num2 = float(input("Type the second number (num2): "))

    # Perform multiplication
    multiplication_result = num1 * num2
    print(f"{num1} * {num2} = {multiplication_result}")

    # Perform division if num2 is not zero
    if num2 != 0:
        division_result = num1 / num2
        print(f"{num1} / {num2} = {division_result}")
    else:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()