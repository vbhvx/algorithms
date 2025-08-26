"""0/1 Knapsack problem solved via 2D dynamic programming."""
from typing import List

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i - 1]; v = values[i - 1]
        for j in range(capacity + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]
