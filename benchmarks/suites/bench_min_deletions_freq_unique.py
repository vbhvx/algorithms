"""
Empirical benchmark for Minimum Deletions Character Frequencies Unique
"""
import time
from algorithms.practice.greedy_algorithms.min_deletions_freq_unique import solve_min_deletions_freq_unique

def benchmark_min_deletions_freq_unique():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_deletions_freq_unique([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_deletions_freq_unique()
    print(f"Minimum Deletions Character Frequencies Unique 100 iterations took {t*1000:.3f}ms")
