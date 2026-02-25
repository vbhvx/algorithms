"""
Empirical benchmark for Replace Substring Balanced String
"""
import time
from algorithms.practice.sliding_window.balanced_substring_rep import solve_balanced_substring_rep

def benchmark_balanced_substring_rep():
    start = time.perf_counter()
    for _ in range(100):
        solve_balanced_substring_rep([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_balanced_substring_rep()
    print(f"Replace Substring Balanced String 100 iterations took {t*1000:.3f}ms")
