#write a python program to print even and odd numbers.
limit = int(input("Enter a number: "))

print("Odd Numbers:")
for num in range(1, limit + 1):
    if num % 2 != 0:
        print(num, end=' ')
        
print("\nEven Numbers:")
for num in range(1, limit + 1):
    if num % 2 == 0:
        print(num, end=' ')
