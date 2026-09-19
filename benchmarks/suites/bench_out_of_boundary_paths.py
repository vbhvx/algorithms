"""
Empirical benchmark for Out of Boundary Paths Grid Movement 1D DP
"""
import time
from algorithms.practice.dynamic_programming_1d.out_of_boundary_paths import solve_out_of_boundary_paths

def benchmark_out_of_boundary_paths():
    start = time.perf_counter()
    for _ in range(100):
        solve_out_of_boundary_paths([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_out_of_boundary_paths()
    print(f"Out of Boundary Paths Grid Movement 1D DP 100 iterations took {t*1000:.3f}ms")
