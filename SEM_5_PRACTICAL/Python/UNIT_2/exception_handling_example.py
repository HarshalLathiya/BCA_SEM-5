# Example: Exception Handling in Python

def divide_numbers(a, b):
    try:
        result = a / b   # This may raise an exception if b = 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero ❌")
    except TypeError:
        print("Error: Please enter only numbers ❌")
    else:
        print("Division successful ✅")
    finally:
        print("Execution completed (finally block runs always).")

# Test Cases
divide_numbers(10, 2)    # Normal case
divide_numbers(5, 0)     # Division by zero case
divide_numbers("5", 2)   # Wrong datatype case
