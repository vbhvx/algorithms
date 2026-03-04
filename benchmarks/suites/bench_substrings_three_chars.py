"""
Empirical benchmark for Substrings Containing All Three Chars
"""
import time
from algorithms.practice.sliding_window.substrings_three_chars import solve_substrings_three_chars

def benchmark_substrings_three_chars():
    start = time.perf_counter()
    for _ in range(100):
        solve_substrings_three_chars([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_substrings_three_chars()
    print(f"Substrings Containing All Three Chars 100 iterations took {t*1000:.3f}ms")
