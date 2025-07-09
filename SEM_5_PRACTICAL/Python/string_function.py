# write a Python program to demonstrate various string functions

text = input("Enter a string: ")

print("Original String: ", text)

print("Length:", len(text))

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Title Case:", text.title())

print("Capitalize:", text.capitalize())

print("Swap Case:", text.swapcase())

char_to_count = input("Enter a character to count: ")
print("Count of '{char_to_count}':", text.count(char_to_count))

substring = input("Enter substring to find: ")
print("First occurrence of '{substring}':", text.find(substring))

old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("After replace:", text.replace(old, new))

start = input("Check if string starts with: ")
print("Starts with?", text.startswith(start))

end = input("Check if string ends with: ")
print("Ends with?", text.endswith(end))

print("Split into words:", text.split())

words = text.split()
print("Joined with '-':", "-".join(words))

print("Is alphabetic?", text.isalpha())


