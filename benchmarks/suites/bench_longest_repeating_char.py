"""
Empirical benchmark for Longest Repeating Character Replace
"""
import time
from algorithms.practice.sliding_window.longest_repeating_char import solve_longest_repeating_char

def benchmark_longest_repeating_char():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_repeating_char([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_repeating_char()
    print(f"Longest Repeating Character Replace 100 iterations took {t*1000:.3f}ms")
