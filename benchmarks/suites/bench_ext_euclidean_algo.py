"""
Empirical benchmark for Extended Euclidean Modular Multiplicative Inverse
"""
import time
from algorithms.practice.math_and_number_theory.ext_euclidean_algo import solve_ext_euclidean_algo

def benchmark_ext_euclidean_algo():
    start = time.perf_counter()
    for _ in range(100):
        solve_ext_euclidean_algo([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ext_euclidean_algo()
    print(f"Extended Euclidean Modular Multiplicative Inverse 100 iterations took {t*1000:.3f}ms")
