"""
Empirical benchmark for Isomorphic Strings Bijective
"""
import time
from algorithms.practice.arrays_and_hashing.isomorphic_strings import solve_isomorphic_strings

def benchmark_isomorphic_strings():
    start = time.perf_counter()
    for _ in range(100):
        solve_isomorphic_strings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_isomorphic_strings()
    print(f"Isomorphic Strings Bijective 100 iterations took {t*1000:.3f}ms")
