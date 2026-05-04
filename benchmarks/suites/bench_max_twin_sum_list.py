"""
Empirical benchmark for Maximum Twin Sum of Linked List
"""
import time
from algorithms.practice.linked_lists.max_twin_sum_list import solve_max_twin_sum_list

def benchmark_max_twin_sum_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_twin_sum_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_twin_sum_list()
    print(f"Maximum Twin Sum of Linked List 100 iterations took {t*1000:.3f}ms")
