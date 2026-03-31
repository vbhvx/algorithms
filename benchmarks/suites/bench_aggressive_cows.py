"""
Empirical benchmark for Aggressive Cows Maximum Minimum Distance
"""
import time
from algorithms.practice.binary_search.aggressive_cows import solve_aggressive_cows

def benchmark_aggressive_cows():
    start = time.perf_counter()
    for _ in range(100):
        solve_aggressive_cows([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_aggressive_cows()
    print(f"Aggressive Cows Maximum Minimum Distance 100 iterations took {t*1000:.3f}ms")
