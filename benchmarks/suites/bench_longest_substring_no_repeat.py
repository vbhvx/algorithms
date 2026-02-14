"""
Empirical benchmark for Longest Substring Without Repeats
"""
import time
from algorithms.practice.sliding_window.longest_substring_no_repeat import solve_longest_substring_no_repeat

def benchmark_longest_substring_no_repeat():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_substring_no_repeat([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_substring_no_repeat()
    print(f"Longest Substring Without Repeats 100 iterations took {t*1000:.3f}ms")
