# Writing to a file
file = open("demo.txt", "w")
file.write("Hello, this is a test file.\nWelcome to Python file handling!")
file.close()

# Reading from the file
file = open("demo.txt", "r")
content = file.read()
file.close()

print("File content:\n", content)
