"""
Empirical benchmark for Equal Substrings Within Budget
"""
import time
from algorithms.practice.sliding_window.equal_substrings_budget import solve_equal_substrings_budget

def benchmark_equal_substrings_budget():
    start = time.perf_counter()
    for _ in range(100):
        solve_equal_substrings_budget([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_equal_substrings_budget()
    print(f"Equal Substrings Within Budget 100 iterations took {t*1000:.3f}ms")
