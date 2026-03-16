"""
Empirical benchmark for Next Greater Element II Circular Stack
"""
import time
from algorithms.practice.stack_and_queue.next_greater_element_ii import solve_next_greater_element_ii

def benchmark_next_greater_element_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_next_greater_element_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_next_greater_element_ii()
    print(f"Next Greater Element II Circular Stack 100 iterations took {t*1000:.3f}ms")
