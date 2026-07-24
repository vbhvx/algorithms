"""
Empirical benchmark for Split String Into Max Unique Substrings
"""
import time
from algorithms.practice.backtracking.split_max_unique_sub import solve_split_max_unique_sub

def benchmark_split_max_unique_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_split_max_unique_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_split_max_unique_sub()
    print(f"Split String Into Max Unique Substrings 100 iterations took {t*1000:.3f}ms")
