"""
Empirical benchmark for Maximum Length Repeated Subarray
"""
import time
from algorithms.practice.sliding_window.max_len_repeated_sub import solve_max_len_repeated_sub

def benchmark_max_len_repeated_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_len_repeated_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_len_repeated_sub()
    print(f"Maximum Length Repeated Subarray 100 iterations took {t*1000:.3f}ms")
