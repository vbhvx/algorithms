"""
Empirical benchmark for House Robber II Circular Boundary Split
"""
import time
from algorithms.practice.dynamic_programming_1d.house_robber_circular import solve_house_robber_circular

def benchmark_house_robber_circular():
    start = time.perf_counter()
    for _ in range(100):
        solve_house_robber_circular([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_house_robber_circular()
    print(f"House Robber II Circular Boundary Split 100 iterations took {t*1000:.3f}ms")
