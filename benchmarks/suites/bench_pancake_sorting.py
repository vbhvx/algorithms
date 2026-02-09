"""
Empirical benchmark for Pancake Sorting Prefix Flips
"""
import time
from algorithms.practice.two_pointers.pancake_sorting import solve_pancake_sorting

def benchmark_pancake_sorting():
    start = time.perf_counter()
    for _ in range(100):
        solve_pancake_sorting([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_pancake_sorting()
    print(f"Pancake Sorting Prefix Flips 100 iterations took {t*1000:.3f}ms")
