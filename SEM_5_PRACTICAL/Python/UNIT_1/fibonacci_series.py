def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b

terms = int(input("Enter how many terms: "))
fibonacci(terms)
