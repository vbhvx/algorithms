"""
Empirical benchmark for Reverse String In Place
"""
import time
from algorithms.practice.two_pointers.reverse_string import solve_reverse_string

def benchmark_reverse_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_string()
    print(f"Reverse String In Place 100 iterations took {t*1000:.3f}ms")
