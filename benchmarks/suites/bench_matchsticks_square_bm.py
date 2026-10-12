"""
Empirical benchmark for Matchsticks to Square Bitmask Memoization
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.matchsticks_square_bm import solve_matchsticks_square_bm

def benchmark_matchsticks_square_bm():
    start = time.perf_counter()
    for _ in range(100):
        solve_matchsticks_square_bm([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_matchsticks_square_bm()
    print(f"Matchsticks to Square Bitmask Memoization 100 iterations took {t*1000:.3f}ms")
