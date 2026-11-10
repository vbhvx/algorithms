"""
Empirical benchmark for Palindrome Number Half Number Reversal
"""
import time
from algorithms.practice.math_and_number_theory.palindrome_number_math import solve_palindrome_number_math

def benchmark_palindrome_number_math():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindrome_number_math([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindrome_number_math()
    print(f"Palindrome Number Half Number Reversal 100 iterations took {t*1000:.3f}ms")
