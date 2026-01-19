"""
Empirical benchmark for Happy Number Cycle Detection
"""
import time
from algorithms.practice.arrays_and_hashing.happy_number import solve_happy_number

def benchmark_happy_number():
    start = time.perf_counter()
    for _ in range(100):
        solve_happy_number([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_happy_number()
    print(f"Happy Number Cycle Detection 100 iterations took {t*1000:.3f}ms")
