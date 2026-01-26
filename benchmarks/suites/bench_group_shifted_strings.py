"""
Empirical benchmark for Group Shifted Strings Canonical
"""
import time
from algorithms.practice.arrays_and_hashing.group_shifted_strings import solve_group_shifted_strings

def benchmark_group_shifted_strings():
    start = time.perf_counter()
    for _ in range(100):
        solve_group_shifted_strings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_group_shifted_strings()
    print(f"Group Shifted Strings Canonical 100 iterations took {t*1000:.3f}ms")
