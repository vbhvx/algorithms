"""
Empirical benchmark for Remove Duplicates from Sorted List
"""
import time
from algorithms.practice.linked_lists.remove_duplicates_sorted import solve_remove_duplicates_sorted

def benchmark_remove_duplicates_sorted():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_duplicates_sorted([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_duplicates_sorted()
    print(f"Remove Duplicates from Sorted List 100 iterations took {t*1000:.3f}ms")
