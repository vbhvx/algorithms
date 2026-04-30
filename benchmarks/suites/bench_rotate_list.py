"""
Empirical benchmark for Rotate List Circular Break Point
"""
import time
from algorithms.practice.linked_lists.rotate_list import solve_rotate_list

def benchmark_rotate_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_rotate_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_rotate_list()
    print(f"Rotate List Circular Break Point 100 iterations took {t*1000:.3f}ms")
