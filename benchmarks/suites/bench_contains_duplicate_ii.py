"""
Empirical benchmark for Contains Duplicate II Window Hash
"""
import time
from algorithms.practice.arrays_and_hashing.contains_duplicate_ii import solve_contains_duplicate_ii

def benchmark_contains_duplicate_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_contains_duplicate_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_contains_duplicate_ii()
    print(f"Contains Duplicate II Window Hash 100 iterations took {t*1000:.3f}ms")
