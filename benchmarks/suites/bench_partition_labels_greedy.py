"""
Empirical benchmark for Partition Labels Last Occurrences Interval
"""
import time
from algorithms.practice.greedy_algorithms.partition_labels_greedy import solve_partition_labels_greedy

def benchmark_partition_labels_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_partition_labels_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_partition_labels_greedy()
    print(f"Partition Labels Last Occurrences Interval 100 iterations took {t*1000:.3f}ms")
