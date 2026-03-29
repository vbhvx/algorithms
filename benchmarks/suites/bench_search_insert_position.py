"""
Empirical benchmark for Search Insert Position Lower Bound
"""
import time
from algorithms.practice.binary_search.search_insert_position import solve_search_insert_position

def benchmark_search_insert_position():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_insert_position([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_insert_position()
    print(f"Search Insert Position Lower Bound 100 iterations took {t*1000:.3f}ms")
