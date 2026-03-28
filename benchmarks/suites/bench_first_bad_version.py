"""
Empirical benchmark for First Bad Version Boundary Search
"""
import time
from algorithms.practice.binary_search.first_bad_version import solve_first_bad_version

def benchmark_first_bad_version():
    start = time.perf_counter()
    for _ in range(100):
        solve_first_bad_version([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_first_bad_version()
    print(f"First Bad Version Boundary Search 100 iterations took {t*1000:.3f}ms")
