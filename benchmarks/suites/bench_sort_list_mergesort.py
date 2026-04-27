"""
Empirical benchmark for Sort List MergeSort Divide and Conquer
"""
import time
from algorithms.practice.linked_lists.sort_list_mergesort import solve_sort_list_mergesort

def benchmark_sort_list_mergesort():
    start = time.perf_counter()
    for _ in range(100):
        solve_sort_list_mergesort([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sort_list_mergesort()
    print(f"Sort List MergeSort Divide and Conquer 100 iterations took {t*1000:.3f}ms")
