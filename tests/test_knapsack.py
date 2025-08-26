from algorithms.dp.knapsack import knapsack_01

def test_knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    assert knapsack_01(weights, values, 50) == 220
