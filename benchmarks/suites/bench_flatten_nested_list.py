"""
Empirical benchmark for Flatten Nested List Iterator Stack
"""
import time
from algorithms.practice.stack_and_queue.flatten_nested_list import solve_flatten_nested_list

def benchmark_flatten_nested_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_flatten_nested_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_flatten_nested_list()
    print(f"Flatten Nested List Iterator Stack 100 iterations took {t*1000:.3f}ms")
