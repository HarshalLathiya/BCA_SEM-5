# Example of Multiple Inheritance in Python

# Parent class 1
class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print("Name:", self.name)

# Parent class 2
class Marks:
    def __init__(self, marks):
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)

# Child class (inherits from Person and Marks)
class Student(Person, Marks):
    def __init__(self, name, marks, roll_no):
        # Call constructors of both parent classes
        Person.__init__(self, name)
        Marks.__init__(self, marks)
        self.roll_no = roll_no

    def show_student(self):
        self.show_person()   # from Person
        self.show_marks()    # from Marks
        print("Roll Number:", self.roll_no)


# Create object of Student
s1 = Student("Harshal", 85, 101)

# Access child method
s1.show_student()
