# Function to perform arithmetic operations
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
        print("Modulus (Remainder):", a % b)
        print("Floor Division:", a // b)
    else:
        print("Division: Cannot divide by zero!")
        print("Modulus: Cannot perform modulus by zero!")
        print("Floor Division: Cannot perform floor division by zero!")

    print("Exponentiation :", a ** b)


# Main Function 
def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        arithmetic_operations(num1, num2)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

main()