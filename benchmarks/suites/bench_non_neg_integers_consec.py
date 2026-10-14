"""
Empirical benchmark for Non-Negative Integers without Consecutive Ones
"""
import time
from algorithms.practice.dynamic_programming_trees_bitmask.non_neg_integers_consec import solve_non_neg_integers_consec

def benchmark_non_neg_integers_consec():
    start = time.perf_counter()
    for _ in range(100):
        solve_non_neg_integers_consec([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_non_neg_integers_consec()
    print(f"Non-Negative Integers without Consecutive Ones 100 iterations took {t*1000:.3f}ms")
