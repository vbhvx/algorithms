"""
Empirical benchmark for Optimize Water Distribution Virtual Wells MST
"""
import time
from algorithms.practice.minimum_spanning_trees.optimize_water_distrib import solve_optimize_water_distrib

def benchmark_optimize_water_distrib():
    start = time.perf_counter()
    for _ in range(100):
        solve_optimize_water_distrib([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_optimize_water_distrib()
    print(f"Optimize Water Distribution Virtual Wells MST 100 iterations took {t*1000:.3f}ms")
