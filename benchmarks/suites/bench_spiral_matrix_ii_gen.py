"""
Empirical benchmark for Spiral Matrix II Layered Value Generation
"""
import time
from algorithms.practice.math_and_number_theory.spiral_matrix_ii_gen import solve_spiral_matrix_ii_gen

def benchmark_spiral_matrix_ii_gen():
    start = time.perf_counter()
    for _ in range(100):
        solve_spiral_matrix_ii_gen([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_spiral_matrix_ii_gen()
    print(f"Spiral Matrix II Layered Value Generation 100 iterations took {t*1000:.3f}ms")
