"""
Empirical benchmark for Find the Duplicate Number Cycle Floyd
"""
import time
from algorithms.practice.linked_lists.find_duplicate_number import solve_find_duplicate_number

def benchmark_find_duplicate_number():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_duplicate_number([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_duplicate_number()
    print(f"Find the Duplicate Number Cycle Floyd 100 iterations took {t*1000:.3f}ms")
