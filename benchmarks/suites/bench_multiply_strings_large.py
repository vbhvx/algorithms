"""
Empirical benchmark for Multiply Strings Large Arithmetic Manual Carry
"""
import time
from algorithms.practice.math_and_number_theory.multiply_strings_large import solve_multiply_strings_large

def benchmark_multiply_strings_large():
    start = time.perf_counter()
    for _ in range(100):
        solve_multiply_strings_large([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_multiply_strings_large()
    print(f"Multiply Strings Large Arithmetic Manual Carry 100 iterations took {t*1000:.3f}ms")
