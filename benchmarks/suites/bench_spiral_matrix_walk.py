"""
Empirical benchmark for Spiral Matrix 4-Boundary Inward Contraction
"""
import time
from algorithms.practice.math_and_number_theory.spiral_matrix_walk import solve_spiral_matrix_walk

def benchmark_spiral_matrix_walk():
    start = time.perf_counter()
    for _ in range(100):
        solve_spiral_matrix_walk([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_spiral_matrix_walk()
    print(f"Spiral Matrix 4-Boundary Inward Contraction 100 iterations took {t*1000:.3f}ms")
