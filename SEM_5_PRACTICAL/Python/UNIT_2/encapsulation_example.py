# Example of Encapsulation (Information Hiding) in Python

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name          # Public variable
        self._roll_no = roll_no   # Protected variable
        self.__marks = marks      # Private variable

    # Getter method for private data
    def get_marks(self):
        return self.__marks

    # Setter method for private data (with validation)
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks! Must be between 0 and 100.")

    # Display info
    def show_info(self):
        print("Name:", self.name)
        print("Roll No:", self._roll_no)
        print("Marks:", self.__marks)


# Create object
s1 = Student("Harshal", 101, 85)

# Access public variable directly
print("Name (Public):", s1.name)

# Access protected variable (possible, but not recommended directly)
print("Roll No (Protected):", s1._roll_no)

# Access private variable directly → Error
# print(s1.__marks) ❌

# Correct way → use getter method
print("Marks (Private via Getter):", s1.get_marks())

# Update marks using setter method
s1.set_marks(92)
s1.show_info()

# Try to set invalid marks
s1.set_marks(150)
