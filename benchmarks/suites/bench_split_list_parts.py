"""
Empirical benchmark for Split Linked List in Parts Length Partition
"""
import time
from algorithms.practice.linked_lists.split_list_parts import solve_split_list_parts

def benchmark_split_list_parts():
    start = time.perf_counter()
    for _ in range(100):
        solve_split_list_parts([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_split_list_parts()
    print(f"Split Linked List in Parts Length Partition 100 iterations took {t*1000:.3f}ms")
