
def fibonacci_bottom_up(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    
    fib = [0] * (n)
    fib[0], fib[1] = 0, 1

    
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci sequence (Bottom-Up DP):")
    print(" ".join(str(x) for x in fibonacci_bottom_up(n)))
