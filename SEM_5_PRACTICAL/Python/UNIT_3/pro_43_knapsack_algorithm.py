# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(weights, values, capacity, n):
    # Create a DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]   # Profit values of items
    weights = [10, 20, 30]    # Weights of items
    capacity = 50             # Maximum capacity of knapsack
    n = len(values)

    max_value = knapsack(weights, values, capacity, n)
    print("Maximum value in Knapsack =", max_value)
