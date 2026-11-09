"""
Empirical benchmark for String to Integer Atoi State Machine Overflow
"""
import time
from algorithms.practice.math_and_number_theory.string_to_integer_atoi import solve_string_to_integer_atoi

def benchmark_string_to_integer_atoi():
    start = time.perf_counter()
    for _ in range(100):
        solve_string_to_integer_atoi([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_string_to_integer_atoi()
    print(f"String to Integer Atoi State Machine Overflow 100 iterations took {t*1000:.3f}ms")
