"""
Empirical benchmark for Kth Smallest Sum of Matrix Rows MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.kth_smallest_sum_matrix import solve_kth_smallest_sum_matrix

def benchmark_kth_smallest_sum_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_smallest_sum_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_smallest_sum_matrix()
    print(f"Kth Smallest Sum of Matrix Rows MinHeap 100 iterations took {t*1000:.3f}ms")
