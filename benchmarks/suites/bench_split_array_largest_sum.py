"""
Empirical benchmark for Split Array Largest Sum Monotonic
"""
import time
from algorithms.practice.binary_search.split_array_largest_sum import solve_split_array_largest_sum

def benchmark_split_array_largest_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_split_array_largest_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_split_array_largest_sum()
    print(f"Split Array Largest Sum Monotonic 100 iterations took {t*1000:.3f}ms")
