"""
Empirical benchmark for Design HashSet Chaining Array
"""
import time
from algorithms.practice.arrays_and_hashing.design_hashset import solve_design_hashset

def benchmark_design_hashset():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_hashset([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_hashset()
    print(f"Design HashSet Chaining Array 100 iterations took {t*1000:.3f}ms")
