"""
Empirical benchmark for Reverse Linked List In Place Iterative
"""
import time
from algorithms.practice.linked_lists.reverse_linked_list import solve_reverse_linked_list

def benchmark_reverse_linked_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_linked_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_linked_list()
    print(f"Reverse Linked List In Place Iterative 100 iterations took {t*1000:.3f}ms")
