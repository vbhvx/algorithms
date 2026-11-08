"""
Empirical benchmark for Pow(x, n) Binary Exponentiation Logarithmic
"""
import time
from algorithms.practice.math_and_number_theory.pow_x_n_binary_exp import solve_pow_x_n_binary_exp

def benchmark_pow_x_n_binary_exp():
    start = time.perf_counter()
    for _ in range(100):
        solve_pow_x_n_binary_exp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_pow_x_n_binary_exp()
    print(f"Pow(x, n) Binary Exponentiation Logarithmic 100 iterations took {t*1000:.3f}ms")
