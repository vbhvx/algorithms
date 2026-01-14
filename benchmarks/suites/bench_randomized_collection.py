"""
Empirical benchmark for Insert Delete GetRandom Duplicates
"""
import time
from algorithms.practice.arrays_and_hashing.randomized_collection import solve_randomized_collection

def benchmark_randomized_collection():
    start = time.perf_counter()
    for _ in range(100):
        solve_randomized_collection([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_randomized_collection()
    print(f"Insert Delete GetRandom Duplicates 100 iterations took {t*1000:.3f}ms")
