try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2   # may raise ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero ❌")
