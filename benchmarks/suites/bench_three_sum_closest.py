"""
Empirical benchmark for 3Sum Closest Target Sum
"""
import time
from algorithms.practice.two_pointers.three_sum_closest import solve_three_sum_closest

def benchmark_three_sum_closest():
    start = time.perf_counter()
    for _ in range(100):
        solve_three_sum_closest([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_three_sum_closest()
    print(f"3Sum Closest Target Sum 100 iterations took {t*1000:.3f}ms")
