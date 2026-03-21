"""
Empirical benchmark for Design Circular Queue Ring Buffer
"""
import time
from algorithms.practice.stack_and_queue.design_circular_queue import solve_design_circular_queue

def benchmark_design_circular_queue():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_circular_queue([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_circular_queue()
    print(f"Design Circular Queue Ring Buffer 100 iterations took {t*1000:.3f}ms")
