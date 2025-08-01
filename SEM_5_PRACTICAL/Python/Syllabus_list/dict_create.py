# Program: 23

car = {"brand": "Toyota", "model": "Camry", "year": 2020}
print("Dict using {}:", car)

student = dict(name="Harshal", age=22, course="BCA")
print("Dict using dict():", student)

empty = {}
print("Empty dict:", empty)

marks = dict([("Java", 90), ("C++", 85)])
print("Dict from list of tuples:", marks)

keys = ["name", "age"]
values = ["Harshal", 21]
person = dict(zip(keys, values))
print("Dict using zip():", person)
