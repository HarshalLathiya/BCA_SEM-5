def is_armstrong(num):
    temp = num
    order = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    return total == num

n = int(input("Enter a number: "))

if is_armstrong(n):
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
