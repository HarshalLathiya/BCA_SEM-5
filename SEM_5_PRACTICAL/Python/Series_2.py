n = int(input("Enter the number of terms: "))
sum = 0

for i in range(1, n + 1):
    sum += i ** 2

print("Sum of the series 1² + 2² + 3² + ... + {}² is: {}".format(n, sum))
