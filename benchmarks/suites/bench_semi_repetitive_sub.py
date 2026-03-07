"""
Empirical benchmark for Longest Semi-Repetitive Substring
"""
import time
from algorithms.practice.sliding_window.semi_repetitive_sub import solve_semi_repetitive_sub

def benchmark_semi_repetitive_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_semi_repetitive_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_semi_repetitive_sub()
    print(f"Longest Semi-Repetitive Substring 100 iterations took {t*1000:.3f}ms")
