"""
Empirical benchmark for Linked List Cycle II Cycle Entry Point
"""
import time
from algorithms.practice.linked_lists.linked_list_cycle_ii import solve_linked_list_cycle_ii

def benchmark_linked_list_cycle_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_linked_list_cycle_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_linked_list_cycle_ii()
    print(f"Linked List Cycle II Cycle Entry Point 100 iterations took {t*1000:.3f}ms")
