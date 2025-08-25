# Example of Private Methods in Python

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks   # private variable

    # Private method
    def __calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"

    # Public method that uses private method
    def show_result(self):
        grade = self.__calculate_grade()   # calling private method
        print(f"Student: {self.name}, Roll No: {self.roll_no}, Marks: {self.__marks}, Grade: {grade}")


# Create object
s1 = Student("Harshal", 101, 88)

# Access public method
s1.show_result()

# Directly calling private method → Error ❌
# s1.__calculate_grade()
