"""
Empirical benchmark for Reverse Linked List II Subsegment M to N
"""
import time
from algorithms.practice.linked_lists.reverse_sublist_ii import solve_reverse_sublist_ii

def benchmark_reverse_sublist_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_sublist_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_sublist_ii()
    print(f"Reverse Linked List II Subsegment M to N 100 iterations took {t*1000:.3f}ms")
