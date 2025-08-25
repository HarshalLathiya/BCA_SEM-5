def fibonacci_memo(n, memo={}):
   
    if n in memo:
        return memo[n]

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci sequence (Top-Down DP):")
    for i in range(n):
        print(fibonacci_memo(i), end=" ")
