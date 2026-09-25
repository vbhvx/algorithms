"""
Empirical benchmark for Longest Common Subsequence 2D Grid
"""
import time
from algorithms.practice.dynamic_programming_2d.longest_common_subseq import solve_longest_common_subseq

def benchmark_longest_common_subseq():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_common_subseq([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_common_subseq()
    print(f"Longest Common Subsequence 2D Grid 100 iterations took {t*1000:.3f}ms")
