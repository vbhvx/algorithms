"""
Empirical benchmark for Insert Delete GetRandom O1
"""
import time
from algorithms.practice.arrays_and_hashing.randomized_set import solve_randomized_set

def benchmark_randomized_set():
    start = time.perf_counter()
    for _ in range(100):
        solve_randomized_set([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_randomized_set()
    print(f"Insert Delete GetRandom O1 100 iterations took {t*1000:.3f}ms")
