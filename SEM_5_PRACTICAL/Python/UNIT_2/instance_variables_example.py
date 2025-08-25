# Example of Instance Variables in Python

class Student:
    def __init__(self, name, roll_no):
        # Instance variables
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)


# Create two objects
s1 = Student("Harshal", 101)
s2 = Student("Gracie", 102)

# Display details
s1.display()
print("---------------")
s2.display()

# Each object has its own copy of instance variables
print("s1 name:", s1.name)
print("s2 name:", s2.name)
