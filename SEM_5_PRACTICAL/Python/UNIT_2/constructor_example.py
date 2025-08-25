# Example of Constructor in Python

class Student:
    # Constructor method
    def __init__(self, name, roll_no):
        self.name = name        # initialize attributes
        self.roll_no = roll_no

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)


# Create objects of Student class (constructor is called automatically)
s1 = Student("Harshal", 101)
s2 = Student("Gracie", 102)

# Display information
s1.display()
print("---------------")
s2.display()
