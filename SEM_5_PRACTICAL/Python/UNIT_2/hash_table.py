# hash_table.py
# Program to demonstrate Hash Table in Python (using dictionary)

# Creating a hash table (Python dictionary)
hash_table = {}

# Inserting key-value pairs
hash_table["101"] = "Alice"
hash_table["102"] = "Bob"
hash_table["103"] = "Charlie"

print("Initial Hash Table:")
for key, value in hash_table.items():
    print(key, ":", value)

# Accessing a value by key
print("\nStudent with ID 102:", hash_table["102"])

# Updating a value
hash_table["103"] = "David"
print("\nUpdated Hash Table:")
for key, value in hash_table.items():
    print(key, ":", value)

# Deleting a key-value pair
del hash_table["101"]
print("\nAfter Deletion:")
for key, value in hash_table.items():
    print(key, ":", value)

# Checking if a key exists
if "102" in hash_table:
    print("\nKey 102 exists in hash table")
