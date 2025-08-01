#input()
name = input("Enter your name: ")

#print()
print("Hello,", name)

#'sep' attribute
print("Python", "is", "fun", sep=" - ")

#'end' attribute
print("This is line 1", end=" | ")
print("This is line 2")

#replacement operator ({})
age = 20
print("Name: {}, Age: {}".format(name, age))
