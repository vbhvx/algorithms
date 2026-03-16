"""
Empirical benchmark for Next Greater Element I Monotonic Hash
"""
import time
from algorithms.practice.stack_and_queue.next_greater_element_i import solve_next_greater_element_i

def benchmark_next_greater_element_i():
    start = time.perf_counter()
    for _ in range(100):
        solve_next_greater_element_i([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_next_greater_element_i()
    print(f"Next Greater Element I Monotonic Hash 100 iterations took {t*1000:.3f}ms")
