"""
Empirical benchmark for Count Special Integers Digit DP Distinct
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.count_special_integers import solve_count_special_integers

def benchmark_count_special_integers():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_special_integers([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_special_integers()
    print(f"Count Special Integers Digit DP Distinct 100 iterations took {t*1000:.3f}ms")
