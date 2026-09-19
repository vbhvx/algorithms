"""
Empirical benchmark for Coin Change II Total Combinations Unbounded
"""
import time
from algorithms.practice.dynamic_programming_1d.coin_change_ii_ways import solve_coin_change_ii_ways

def benchmark_coin_change_ii_ways():
    start = time.perf_counter()
    for _ in range(100):
        solve_coin_change_ii_ways([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_coin_change_ii_ways()
    print(f"Coin Change II Total Combinations Unbounded 100 iterations took {t*1000:.3f}ms")
