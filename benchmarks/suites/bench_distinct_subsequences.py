"""
Empirical benchmark for Distinct Subsequences 2D String Match
"""
import time
from algorithms.practice.dynamic_programming_2d.distinct_subsequences import solve_distinct_subsequences

def benchmark_distinct_subsequences():
    start = time.perf_counter()
    for _ in range(100):
        solve_distinct_subsequences([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_distinct_subsequences()
    print(f"Distinct Subsequences 2D String Match 100 iterations took {t*1000:.3f}ms")
