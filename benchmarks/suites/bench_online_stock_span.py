"""
Empirical benchmark for Online Stock Span Monotonic Stack
"""
import time
from algorithms.practice.stack_and_queue.online_stock_span import solve_online_stock_span

def benchmark_online_stock_span():
    start = time.perf_counter()
    for _ in range(100):
        solve_online_stock_span([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_online_stock_span()
    print(f"Online Stock Span Monotonic Stack 100 iterations took {t*1000:.3f}ms")
