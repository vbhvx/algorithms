"""
Empirical benchmark for Design HashMap Chaining Array
"""
import time
from algorithms.practice.arrays_and_hashing.design_hashmap import solve_design_hashmap

def benchmark_design_hashmap():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_hashmap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_hashmap()
    print(f"Design HashMap Chaining Array 100 iterations took {t*1000:.3f}ms")
