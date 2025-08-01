def number_triangle():
    for i in range(1, 6):
        print(str(i) * i)

def alphabet_triangle():
    for i in range(1, 6):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()

def reverse_star():
    for i in range(5, 0, -1):
        print("*" * i)

while True:
    print("1. Number Triangle")
    print("2. Alphabet Triangle")
    print("3. Reverse Star Pattern")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nNumber Triangle:")
        number_triangle()

    elif choice == '2':
        print("\nAlphabet Triangle:")
        alphabet_triangle()

    elif choice == '3':
        print("\nReverse Star Pattern:")
        reverse_star()

    elif choice == '4':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
