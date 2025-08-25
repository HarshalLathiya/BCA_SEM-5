# Example of Inheritance in Python

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, roll_no):
        # Call parent constructor
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        # Access parent method
        self.display_person()
        print("Roll Number:", self.roll_no)


# Create object of Student
s1 = Student("Harshal", 20, 101)

# Call child class method
s1.display_student()
