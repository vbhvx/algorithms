"""
Empirical benchmark for Count Ways to Build Good Strings Modular DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.ways_build_good_strings import solve_ways_build_good_strings

def benchmark_ways_build_good_strings():
    start = time.perf_counter()
    for _ in range(100):
        solve_ways_build_good_strings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ways_build_good_strings()
    print(f"Count Ways to Build Good Strings Modular DP 100 iterations took {t*1000:.3f}ms")
