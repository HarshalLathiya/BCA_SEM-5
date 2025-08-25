# Example of Class Variables (Static Variables) in Python

class Student:
    # Class variable (shared by all objects)
    college_name = "KSC - Amreli"

    def __init__(self, name, roll_no):
        # Instance variables
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        # Access class variable
        print("College:", Student.college_name)


# Create objects
s1 = Student("Harshal", 101)
s2 = Student("Gracie", 102)

# Display details
s1.display()
print("---------------")
s2.display()

# Access class variable directly using class
print("College Name (via class):", Student.college_name)

# Change class variable
Student.college_name = "XYZ University"

print("\nAfter Changing College Name:")

s1.display()
s2.display()
