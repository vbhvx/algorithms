"""
Empirical benchmark for Wildcard Matching Question Mark Star
"""
import time
from algorithms.practice.dynamic_programming_2d.wildcard_matching_2d import solve_wildcard_matching_2d

def benchmark_wildcard_matching_2d():
    start = time.perf_counter()
    for _ in range(100):
        solve_wildcard_matching_2d([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_wildcard_matching_2d()
    print(f"Wildcard Matching Question Mark Star 100 iterations took {t*1000:.3f}ms")
