"""
Empirical benchmark for Circular Array Loop Slow Fast
"""
import time
from algorithms.practice.two_pointers.circular_array_loop import solve_circular_array_loop

def benchmark_circular_array_loop():
    start = time.perf_counter()
    for _ in range(100):
        solve_circular_array_loop([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_circular_array_loop()
    print(f"Circular Array Loop Slow Fast 100 iterations took {t*1000:.3f}ms")
