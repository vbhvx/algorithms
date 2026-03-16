"""
Empirical benchmark for Sum of Subarray Minimums Monotonic
"""
import time
from algorithms.practice.stack_and_queue.sum_subarray_mins import solve_sum_subarray_mins

def benchmark_sum_subarray_mins():
    start = time.perf_counter()
    for _ in range(100):
        solve_sum_subarray_mins([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sum_subarray_mins()
    print(f"Sum of Subarray Minimums Monotonic 100 iterations took {t*1000:.3f}ms")
