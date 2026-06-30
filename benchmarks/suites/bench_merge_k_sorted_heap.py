"""
Empirical benchmark for Merge K Sorted Lists MinHeap Priority
"""
import time
from algorithms.practice.heaps_and_priority.merge_k_sorted_heap import solve_merge_k_sorted_heap

def benchmark_merge_k_sorted_heap():
    start = time.perf_counter()
    for _ in range(100):
        solve_merge_k_sorted_heap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_merge_k_sorted_heap()
    print(f"Merge K Sorted Lists MinHeap Priority 100 iterations took {t*1000:.3f}ms")
