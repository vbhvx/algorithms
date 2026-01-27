"""
Empirical benchmark for 3Sum Zero Triplet Two Pointers
"""
import time
from algorithms.practice.two_pointers.three_sum import solve_three_sum

def benchmark_three_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_three_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_three_sum()
    print(f"3Sum Zero Triplet Two Pointers 100 iterations took {t*1000:.3f}ms")
