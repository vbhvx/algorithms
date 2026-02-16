"""
Empirical benchmark for Minimum Window Substring Shrink
"""
import time
from algorithms.practice.sliding_window.minimum_window_substring import solve_minimum_window_substring

def benchmark_minimum_window_substring():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimum_window_substring([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimum_window_substring()
    print(f"Minimum Window Substring Shrink 100 iterations took {t*1000:.3f}ms")
