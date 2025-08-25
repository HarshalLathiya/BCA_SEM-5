#program:-40
# Example of Encapsulation in Python

class Student:
    def __init__(self, name, age):
        # Public member
        self.name = name

        # Private member (accessible only inside the class)
        self.__age = age  

    # Public method to get private data
    def get_age(self):
        return self.__age

    # Public method to update private data
    def set_age(self, age):
        if age > 0:   # simple validation
            self.__age = age
        else:
            print("Invalid age!")


# Create object of Student
s1 = Student("Harshal", 20)

# Accessing public variable directly
print("Name:", s1.name)

# Accessing private variable directly will give error:
# print(s1.__age) ❌

# Correct way: use getter method
print("Age:", s1.get_age())

# Update age using setter method
s1.set_age(21)
print("Updated Age:", s1.get_age())

# Trying to set invalid age
s1.set_age(-5)
