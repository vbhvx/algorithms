"""
Empirical benchmark for 3Sum Smaller Target Triplet Count
"""
import time
from algorithms.practice.two_pointers.three_sum_smaller import solve_three_sum_smaller

def benchmark_three_sum_smaller():
    start = time.perf_counter()
    for _ in range(100):
        solve_three_sum_smaller([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_three_sum_smaller()
    print(f"3Sum Smaller Target Triplet Count 100 iterations took {t*1000:.3f}ms")
