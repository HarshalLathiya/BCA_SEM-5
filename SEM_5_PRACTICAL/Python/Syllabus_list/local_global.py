lang = "Python"  # Global variable

def show():
    lang = "Java"  # Local variable
    print("Inside function:", lang)

show()
print("Outside function:", lang)
