"""
Empirical benchmark for Flatten Multilevel Doubly Linked List
"""
import time
from algorithms.practice.linked_lists.flatten_multilevel_dll import solve_flatten_multilevel_dll

def benchmark_flatten_multilevel_dll():
    start = time.perf_counter()
    for _ in range(100):
        solve_flatten_multilevel_dll([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_flatten_multilevel_dll()
    print(f"Flatten Multilevel Doubly Linked List 100 iterations took {t*1000:.3f}ms")
