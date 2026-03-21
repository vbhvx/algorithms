"""
Empirical benchmark for Max Stack Dual Stack Tracking
"""
import time
from algorithms.practice.stack_and_queue.max_stack import solve_max_stack

def benchmark_max_stack():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_stack([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_stack()
    print(f"Max Stack Dual Stack Tracking 100 iterations took {t*1000:.3f}ms")
