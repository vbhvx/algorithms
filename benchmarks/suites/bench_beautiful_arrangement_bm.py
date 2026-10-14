"""
Empirical benchmark for Beautiful Arrangement Bitmask DP
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.beautiful_arrangement_bm import solve_beautiful_arrangement_bm

def benchmark_beautiful_arrangement_bm():
    start = time.perf_counter()
    for _ in range(100):
        solve_beautiful_arrangement_bm([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_beautiful_arrangement_bm()
    print(f"Beautiful Arrangement Bitmask DP 100 iterations took {t*1000:.3f}ms")
