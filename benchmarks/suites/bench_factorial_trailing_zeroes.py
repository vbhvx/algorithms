"""
Empirical benchmark for Factorial Trailing Zeroes Legendre Multiples of 5
"""
import time
from algorithms.practice.math_and_number_theory.factorial_trailing_zeroes import solve_factorial_trailing_zeroes

def benchmark_factorial_trailing_zeroes():
    start = time.perf_counter()
    for _ in range(100):
        solve_factorial_trailing_zeroes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_factorial_trailing_zeroes()
    print(f"Factorial Trailing Zeroes Legendre Multiples of 5 100 iterations took {t*1000:.3f}ms")
