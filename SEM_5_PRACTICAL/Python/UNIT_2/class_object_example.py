# Example of Class and Object in Python

# Define a class
class Student:
    # Constructor (called when object is created)
    def __init__(self, name, roll_no):
        self.name = name       # attribute
        self.roll_no = roll_no # attribute

    # Method to display student details
    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


# Create objects of Student class
s1 = Student("Harshal", 101)
s2 = Student("Gracie", 102)

# Call method using objects
s1.display_info()
print("----------------")
s2.display_info()
