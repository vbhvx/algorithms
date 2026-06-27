"""
Empirical benchmark for Reorganize String MaxHeap Greedy Spacing
"""
import time
from algorithms.practice.heaps_and_priority.reorganize_string import solve_reorganize_string

def benchmark_reorganize_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_reorganize_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reorganize_string()
    print(f"Reorganize String MaxHeap Greedy Spacing 100 iterations took {t*1000:.3f}ms")
