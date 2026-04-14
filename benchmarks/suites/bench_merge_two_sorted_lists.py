"""
Empirical benchmark for Merge Two Sorted Lists Iterative
"""
import time
from algorithms.practice.linked_lists.merge_two_sorted_lists import solve_merge_two_sorted_lists

def benchmark_merge_two_sorted_lists():
    start = time.perf_counter()
    for _ in range(100):
        solve_merge_two_sorted_lists([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_merge_two_sorted_lists()
    print(f"Merge Two Sorted Lists Iterative 100 iterations took {t*1000:.3f}ms")
