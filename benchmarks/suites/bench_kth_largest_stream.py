"""
Empirical benchmark for Kth Largest Element in a Stream MinHeap
"""
import time
from algorithms.practice.heaps_and_priority.kth_largest_stream import solve_kth_largest_stream

def benchmark_kth_largest_stream():
    start = time.perf_counter()
    for _ in range(100):
        solve_kth_largest_stream([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_kth_largest_stream()
    print(f"Kth Largest Element in a Stream MinHeap 100 iterations took {t*1000:.3f}ms")
