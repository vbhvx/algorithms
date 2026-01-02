"""
Empirical benchmark for Longest Consecutive Sequence Set
"""
import time
from algorithms.practice.arrays_and_hashing.longest_consecutive import solve_longest_consecutive

def benchmark_longest_consecutive():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_consecutive([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_consecutive()
    print(f"Longest Consecutive Sequence Set 100 iterations took {t*1000:.3f}ms")
