"""
Empirical benchmark for Sum of Subarray Ranges Monotonic Pair
"""
import time
from algorithms.practice.stack_and_queue.sum_subarray_ranges import solve_sum_subarray_ranges

def benchmark_sum_subarray_ranges():
    start = time.perf_counter()
    for _ in range(100):
        solve_sum_subarray_ranges([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sum_subarray_ranges()
    print(f"Sum of Subarray Ranges Monotonic Pair 100 iterations took {t*1000:.3f}ms")
