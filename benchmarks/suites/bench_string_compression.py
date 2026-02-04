"""
Empirical benchmark for String Compression In Place
"""
import time
from algorithms.practice.two_pointers.string_compression import solve_string_compression

def benchmark_string_compression():
    start = time.perf_counter()
    for _ in range(100):
        solve_string_compression([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_string_compression()
    print(f"String Compression In Place 100 iterations took {t*1000:.3f}ms")
