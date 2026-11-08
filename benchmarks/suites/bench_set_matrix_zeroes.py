"""
Empirical benchmark for Set Matrix Zeroes First Row Column Marker
"""
import time
from algorithms.practice.math_and_number_theory.set_matrix_zeroes import solve_set_matrix_zeroes

def benchmark_set_matrix_zeroes():
    start = time.perf_counter()
    for _ in range(100):
        solve_set_matrix_zeroes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_set_matrix_zeroes()
    print(f"Set Matrix Zeroes First Row Column Marker 100 iterations took {t*1000:.3f}ms")
