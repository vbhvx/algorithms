"""
Empirical benchmark for Partition Labels Last Seen Index
"""
import time
from algorithms.practice.two_pointers.partition_labels import solve_partition_labels

def benchmark_partition_labels():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_labels([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_labels()
    print(f"Partition Labels Last Seen Index 100 iterations took {t*1000:.3f}ms")
