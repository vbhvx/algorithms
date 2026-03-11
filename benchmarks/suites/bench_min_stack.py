"""
Empirical benchmark for Min Stack O1 Operations
"""
import time
from algorithms.practice.stack_and_queue.min_stack import solve_min_stack

def benchmark_min_stack():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_stack([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_stack()
    print(f"Min Stack O1 Operations 100 iterations took {t*1000:.3f}ms")
