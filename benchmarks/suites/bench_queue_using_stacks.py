"""
Empirical benchmark for Implement Queue using Stacks Amortized
"""
import time
from algorithms.practice.stack_and_queue.queue_using_stacks import solve_queue_using_stacks

def benchmark_queue_using_stacks():
    start = time.perf_counter()
    for _ in range(100):
        solve_queue_using_stacks([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_queue_using_stacks()
    print(f"Implement Queue using Stacks Amortized 100 iterations took {t*1000:.3f}ms")
