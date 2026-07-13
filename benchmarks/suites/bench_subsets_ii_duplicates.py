"""
Empirical benchmark for Subsets II with Duplicates Skip Sorted
"""
import time
from algorithms.practice.backtracking.subsets_ii_duplicates import solve_subsets_ii_duplicates

def benchmark_subsets_ii_duplicates():
    start = time.perf_counter()
    for _ in range(100):
        solve_subsets_ii_duplicates([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_subsets_ii_duplicates()
    print(f"Subsets II with Duplicates Skip Sorted 100 iterations took {t*1000:.3f}ms")
