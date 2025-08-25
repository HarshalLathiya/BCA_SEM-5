# Fibonacci with Dynamic Programming (Memoization)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Test
n = 10
print(f"Fibonacci({n}) =", fib(n))
