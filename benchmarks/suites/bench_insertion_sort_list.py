"""
Empirical benchmark for Insertion Sort List Pointer Splice
"""
import time
from algorithms.practice.linked_lists.insertion_sort_list import solve_insertion_sort_list

def benchmark_insertion_sort_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_insertion_sort_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_insertion_sort_list()
    print(f"Insertion Sort List Pointer Splice 100 iterations took {t*1000:.3f}ms")
