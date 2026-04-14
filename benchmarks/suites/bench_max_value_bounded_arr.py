"""
Empirical benchmark for Maximum Value at Given Index Bounded Array
"""
import time
from algorithms.practice.binary_search.max_value_bounded_arr import solve_max_value_bounded_arr

def benchmark_max_value_bounded_arr():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_value_bounded_arr([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_value_bounded_arr()
    print(f"Maximum Value at Given Index Bounded Array 100 iterations took {t*1000:.3f}ms")
