"""
Empirical benchmark for Non-Decreasing Subsequences Hash Visited
"""
import time
from algorithms.practice.backtracking.non_decreasing_subseq import solve_non_decreasing_subseq

def benchmark_non_decreasing_subseq():
    start = time.perf_counter()
    for _ in range(100):
        solve_non_decreasing_subseq([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_non_decreasing_subseq()
    print(f"Non-Decreasing Subsequences Hash Visited 100 iterations took {t*1000:.3f}ms")
