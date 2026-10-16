"""
Empirical benchmark for All Possible Full Binary Trees Catalan DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.all_possible_full_binary import solve_all_possible_full_binary

def benchmark_all_possible_full_binary():
    start = time.perf_counter()
    for _ in range(100):
        solve_all_possible_full_binary([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_all_possible_full_binary()
    print(f"All Possible Full Binary Trees Catalan DP 100 iterations took {t*1000:.3f}ms")
