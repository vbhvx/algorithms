"""
Empirical benchmark for Reorder List Reverse Second Half Interleave
"""
import time
from algorithms.practice.linked_lists.reorder_list import solve_reorder_list

def benchmark_reorder_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_reorder_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reorder_list()
    print(f"Reorder List Reverse Second Half Interleave 100 iterations took {t*1000:.3f}ms")
