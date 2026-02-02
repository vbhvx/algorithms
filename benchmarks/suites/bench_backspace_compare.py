"""
Empirical benchmark for Backspace String Compare Reverse
"""
import time
from algorithms.practice.two_pointers.backspace_compare import solve_backspace_compare

def benchmark_backspace_compare():
    start = time.perf_counter()
    for _ in range(100):
        solve_backspace_compare([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_backspace_compare()
    print(f"Backspace String Compare Reverse 100 iterations took {t*1000:.3f}ms")
