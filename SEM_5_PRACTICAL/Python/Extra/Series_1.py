n = int(input("Enter the number of terms: "))
sum = 0.0

for i in range(1, n + 1):
    sum += 1 / i

print("Sum of the series 1/1 + 1/2 + 1/3 + ... + 1/{} is: {:.4f}".format(n, sum))
