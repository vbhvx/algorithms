"""
Empirical benchmark for Odd Even Linked List Grouping
"""
import time
from algorithms.practice.linked_lists.odd_even_linked_list import solve_odd_even_linked_list

def benchmark_odd_even_linked_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_odd_even_linked_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_odd_even_linked_list()
    print(f"Odd Even Linked List Grouping 100 iterations took {t*1000:.3f}ms")
