# Program Name: assert_example.py

def calculate_average(marks):
    # Assert that marks list is not empty
    assert len(marks) > 0, "Marks list cannot be empty!"
    
    # Assert that all marks are positive
    for mark in marks:
        assert mark >= 0, "Marks cannot be negative!"
    
    total = sum(marks)
    avg = total / len(marks)
    return avg

# Main program
try:
    marks = [80, 90, 75, 85]   # Valid data
    print("Marks:", marks)
    print("Average:", calculate_average(marks))
    
    # Uncomment below to see assertion error examples:
    # marks = []  # Will trigger "Marks list cannot be empty!"
    # marks = [80, -5, 90]  # Will trigger "Marks cannot be negative!"
    
except AssertionError as e:
    print("Assertion Error:", e)
