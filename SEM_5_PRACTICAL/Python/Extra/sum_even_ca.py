import sys

even_sum = 0
for arg in sys.argv[1:]:
    num = int(arg)
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:", even_sum)
