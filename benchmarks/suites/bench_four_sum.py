"""
Empirical benchmark for 4Sum Quadruplet Two Pointers
"""
import time
from algorithms.practice.two_pointers.four_sum import solve_four_sum

def benchmark_four_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_four_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_four_sum()
    print(f"4Sum Quadruplet Two Pointers 100 iterations took {t*1000:.3f}ms")
