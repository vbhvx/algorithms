"""
Empirical benchmark for Majority Element Boyer Moore
"""
import time
from algorithms.practice.arrays_and_hashing.majority_element_boyer import solve_majority_element_boyer

def benchmark_majority_element_boyer():
    start = time.perf_counter()
    for _ in range(100):
        solve_majority_element_boyer([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_majority_element_boyer()
    print(f"Majority Element Boyer Moore 100 iterations took {t*1000:.3f}ms")
