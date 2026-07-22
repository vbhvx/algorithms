"""
Empirical benchmark for Count Numbers with Unique Digits Combinatorics
"""
import time
from algorithms.practice.backtracking.numbers_unique_digits import solve_numbers_unique_digits

def benchmark_numbers_unique_digits():
    start = time.perf_counter()
    for _ in range(100):
        solve_numbers_unique_digits([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_numbers_unique_digits()
    print(f"Count Numbers with Unique Digits Combinatorics 100 iterations took {t*1000:.3f}ms")
