"""
Empirical benchmark for Valid Perfect Square Logarithmic
"""
import time
from algorithms.practice.binary_search.valid_perfect_square import solve_valid_perfect_square

def benchmark_valid_perfect_square():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_perfect_square([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_perfect_square()
    print(f"Valid Perfect Square Logarithmic 100 iterations took {t*1000:.3f}ms")
