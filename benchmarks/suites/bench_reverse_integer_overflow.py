"""
Empirical benchmark for Reverse Integer Math Pop Push Overflow Check
"""
import time
from algorithms.practice.math_and_number_theory.reverse_integer_overflow import solve_reverse_integer_overflow

def benchmark_reverse_integer_overflow():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_integer_overflow([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_integer_overflow()
    print(f"Reverse Integer Math Pop Push Overflow Check 100 iterations took {t*1000:.3f}ms")
