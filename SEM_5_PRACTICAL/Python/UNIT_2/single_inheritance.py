# Example of Single Inheritance in Python

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Child class (inherits Person)
class Student(Person):
    def __init__(self, name, age, roll_no):
        # Call parent constructor
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_student(self):
        # Call parent method
        self.show_person()
        print("Roll Number:", self.roll_no)


# Create object of Student (child class)
s1 = Student("Harshal", 20, 101)

# Access methods
s1.show_student()
