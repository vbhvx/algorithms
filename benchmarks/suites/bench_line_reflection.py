"""
Empirical benchmark for Line Reflection Coordinate Set
"""
import time
from algorithms.practice.arrays_and_hashing.line_reflection import solve_line_reflection

def benchmark_line_reflection():
    start = time.perf_counter()
    for _ in range(100):
        solve_line_reflection([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_line_reflection()
    print(f"Line Reflection Coordinate Set 100 iterations took {t*1000:.3f}ms")
