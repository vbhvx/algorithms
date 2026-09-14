"""
Empirical benchmark for Coin Change Unbounded Minimum Coins
"""
import time
from algorithms.practice.dynamic_programming_1d.coin_change_min import solve_coin_change_min

def benchmark_coin_change_min():
    start = time.perf_counter()
    for _ in range(100):
        solve_coin_change_min([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_coin_change_min()
    print(f"Coin Change Unbounded Minimum Coins 100 iterations took {t*1000:.3f}ms")
