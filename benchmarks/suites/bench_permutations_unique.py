"""
Empirical benchmark for Permutations Array In-Place Swap
"""
import time
from algorithms.practice.backtracking.permutations_unique import solve_permutations_unique

def benchmark_permutations_unique():
    start = time.perf_counter()
    for _ in range(100):
        solve_permutations_unique([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_permutations_unique()
    print(f"Permutations Array In-Place Swap 100 iterations took {t*1000:.3f}ms")
