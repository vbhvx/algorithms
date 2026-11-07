"""
Empirical benchmark for Rotate Image 90 Degrees In-Place Transpose
"""
import time
from algorithms.practice.math_and_number_theory.rotate_image_matrix import solve_rotate_image_matrix

def benchmark_rotate_image_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_rotate_image_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_rotate_image_matrix()
    print(f"Rotate Image 90 Degrees In-Place Transpose 100 iterations took {t*1000:.3f}ms")
