"""
Empirical benchmark for Array Partition Min Pair Sum
"""
import time
from algorithms.practice.two_pointers.array_partition import solve_array_partition

def benchmark_array_partition():
    start = time.perf_counter()
    for _ in range(100):
        solve_array_partition([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_array_partition()
    print(f"Array Partition Min Pair Sum 100 iterations took {t*1000:.3f}ms")
