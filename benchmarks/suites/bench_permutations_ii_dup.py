"""
Empirical benchmark for Permutations II Duplicate Elements Skip
"""
import time
from algorithms.practice.backtracking.permutations_ii_dup import solve_permutations_ii_dup

def benchmark_permutations_ii_dup():
    start = time.perf_counter()
    for _ in range(100):
        solve_permutations_ii_dup([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_permutations_ii_dup()
    print(f"Permutations II Duplicate Elements Skip 100 iterations took {t*1000:.3f}ms")
