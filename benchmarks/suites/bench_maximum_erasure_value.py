"""
Empirical benchmark for Maximum Erasure Value Unique Window
"""
import time
from algorithms.practice.sliding_window.maximum_erasure_value import solve_maximum_erasure_value

def benchmark_maximum_erasure_value():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximum_erasure_value([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximum_erasure_value()
    print(f"Maximum Erasure Value Unique Window 100 iterations took {t*1000:.3f}ms")
