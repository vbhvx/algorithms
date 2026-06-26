"""
Empirical benchmark for Kth Largest Element in Array QuickSelect MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.kth_largest_array import solve_kth_largest_array

def benchmark_kth_largest_array():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_largest_array([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_largest_array()
    print(f"Kth Largest Element in Array QuickSelect MinHeap 100 iterations took {t*1000:.3f}ms")
