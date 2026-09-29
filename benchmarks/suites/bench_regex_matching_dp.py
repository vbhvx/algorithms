"""
Empirical benchmark for Regular Expression Matching Wildcard Star
"""
import time
from algorithms.practice.dynamic_programming_2d.regex_matching_dp import solve_regex_matching_dp

def benchmark_regex_matching_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_regex_matching_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_regex_matching_dp()
    print(f"Regular Expression Matching Wildcard Star 100 iterations took {t*1000:.3f}ms")
