#program 16
# Using square brackets []
fruits = ["apple", "banana", "cherry"]
print("List using []:", fruits)

#Using list() constructor
nums = list((1, 2, 3, 4)) 
print("List using list():", nums)

#Creating empty list
empty = []
print("Empty list:", empty)

#Using list comprehension
squares = [x*x for x in range(1, 6)]
print("List using comprehension:", squares)

#From a string 
chars = list("hello")
print("List from string:", chars)

#From a range
rng_list = list(range(5))
print("List from range():", rng_list)
