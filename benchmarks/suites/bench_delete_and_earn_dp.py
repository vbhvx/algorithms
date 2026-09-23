"""
Empirical benchmark for Delete and Earn House Robber Transformation
"""
import time
from algorithms.practice.dynamic_programming_1d.delete_and_earn_dp import solve_delete_and_earn_dp

def benchmark_delete_and_earn_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_delete_and_earn_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_delete_and_earn_dp()
    print(f"Delete and Earn House Robber Transformation 100 iterations took {t*1000:.3f}ms")
