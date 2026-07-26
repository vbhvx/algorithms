"""
Empirical benchmark for Pacific Atlantic Water Flow Inverse Reach
"""
import time
from algorithms.practice.graphs_and_traversals.pacific_atlantic import solve_pacific_atlantic

def benchmark_pacific_atlantic():
    start = time.perf_counter()
    for _ in range(100):
        solve_pacific_atlantic([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_pacific_atlantic()
    print(f"Pacific Atlantic Water Flow Inverse Reach 100 iterations took {t*1000:.3f}ms")
