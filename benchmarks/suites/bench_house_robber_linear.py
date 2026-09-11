"""
Empirical benchmark for House Robber Non-Adjacent Maximization
"""
import time
from algorithms.practice.dynamic_programming_1d.house_robber_linear import solve_house_robber_linear

def benchmark_house_robber_linear():
    start = time.perf_counter()
    for _ in range(100):
        solve_house_robber_linear([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_house_robber_linear()
    print(f"House Robber Non-Adjacent Maximization 100 iterations took {t*1000:.3f}ms")
