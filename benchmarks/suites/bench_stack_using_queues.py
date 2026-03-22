"""
Empirical benchmark for Implement Stack using Queues
"""
import time
from algorithms.practice.stack_and_queue.stack_using_queues import solve_stack_using_queues

def benchmark_stack_using_queues():
    start = time.perf_counter()
    for _ in range(100):
        solve_stack_using_queues([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stack_using_queues()
    print(f"Implement Stack using Queues 100 iterations took {t*1000:.3f}ms")
