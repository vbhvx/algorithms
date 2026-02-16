"""
Empirical benchmark for Permutation in String Window
"""
import time
from algorithms.practice.sliding_window.permutation_string import solve_permutation_string

def benchmark_permutation_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_permutation_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_permutation_string()
    print(f"Permutation in String Window 100 iterations took {t*1000:.3f}ms")
