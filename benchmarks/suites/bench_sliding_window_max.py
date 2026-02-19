"""
Empirical benchmark for Sliding Window Maximum Monotonic Deque
"""
import time
from algorithms.practice.sliding_window.sliding_window_max import solve_sliding_window_max

def benchmark_sliding_window_max():
    start = time.perf_counter()
    for _ in range(100):
        solve_sliding_window_max([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sliding_window_max()
    print(f"Sliding Window Maximum Monotonic Deque 100 iterations took {t*1000:.3f}ms")
