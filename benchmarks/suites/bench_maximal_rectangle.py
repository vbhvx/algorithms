"""
Empirical benchmark for Maximal Rectangle 2D Binary Matrix
"""
import time
from algorithms.practice.stack_and_queue.maximal_rectangle import solve_maximal_rectangle

def benchmark_maximal_rectangle():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximal_rectangle([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximal_rectangle()
    print(f"Maximal Rectangle 2D Binary Matrix 100 iterations took {t*1000:.3f}ms")
