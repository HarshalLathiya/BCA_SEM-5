# Creating a list
my_list = ["Harshal", "BCA", "Freelancer", "HTML", "CSS"]
print("Original List:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Sliced List (index 1 to 3):", my_list[1:4])

# Adding elements
my_list.append("GitHub")  # Adds at the end
print("After append:", my_list)

my_list.insert(2, "Semester 5")  # Inserts at index 2
print("After insert:", my_list)

# Extending list
my_list.extend(["Node.js", "Express.js"])
print("After extend:", my_list)

# Removing elements
my_list.remove("CSS")  # Removes by value
print("After remove:", my_list)

popped_item = my_list.pop()    # Removes last item
print("After pop:", my_list)
print("Popped item:", popped_item)

# Updating elements
my_list[0] = "Harshal Lathiya"
print("After updating first element:", my_list)

# Searching elements
print("Is 'Python' in list?", "Python" in my_list)

# Length of list
print("Length of list:", len(my_list))

# Sorting and reversing
numbers = [3, 1, 4, 2, 5]
print("\nNumbers list before sort:", numbers)
numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

# Copying list
copied_list = my_list.copy()
print("\nCopied List:", copied_list)

# Clearing list
my_list.clear()
print("After clear (empty list):", my_list)
