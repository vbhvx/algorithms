"""
Empirical benchmark for Partition List Preserving Relative Order
"""
import time
from algorithms.practice.linked_lists.partition_list import solve_partition_list

def benchmark_partition_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_list()
    print(f"Partition List Preserving Relative Order 100 iterations took {t*1000:.3f}ms")
