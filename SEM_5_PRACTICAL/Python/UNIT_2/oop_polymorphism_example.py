# Polymorphism Mix Example in Python

# Base class (Parent)
class Person:
    college_name = "KSC - Amreli"   # Class Variable (shared by all)

    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    # Method to be overridden
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Person.college_name)


# Child class 1
class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)   # call parent constructor
        self.roll_no = roll_no
        self.marks = marks

    # Overriding method (Polymorphism)
    def show_info(self):
        print("---- Student Info ----")
        super().show_info()
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Child class 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Overriding method (Polymorphism)
    def show_info(self):
        print("---- Teacher Info ----")
        super().show_info()
        print("Subject:", self.subject)


# Child class 3
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    # Overriding method (Polymorphism)
    def show_info(self):
        print("---- Staff Info ----")
        super().show_info()
        print("Department:", self.department)


# Polymorphism in action
people = [
    Student("Harshal", 20, 101, 85),
    Teacher("Nilesh Sir", 35, "Python"),
    Staff("Paresh Bhai", 40, "Administration")
]

# Same method call behaves differently for each object
for p in people:
    p.show_info()
    print("-----------------------")
