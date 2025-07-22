# for loop – print even numbers up to user input

limit = int(input("Enter a limit for even numbers: "))
print("Even numbers from 1 to", limit)
for num in range(1, limit + 1):
    if num % 2 == 0:
        print(num)

 # while loop – print even numbers up to user-specified limit and calculate their sum

limit = int(input("Enter a limit for while loop: "))
i = 1
sum_even = 0

print("Even numbers from 1 to", limit, "are:")

while i <= limit:
    if i % 2 == 0:
        print(i)
        sum_even += i
    i += 1

print("Sum of even numbers from 1 to", limit, "is:", sum_even)
       
