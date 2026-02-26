"""
Empirical benchmark for Max Vowels in Substring K
"""
import time
from algorithms.practice.sliding_window.max_vowels_substring import solve_max_vowels_substring

def benchmark_max_vowels_substring():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_vowels_substring([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_vowels_substring()
    print(f"Max Vowels in Substring K 100 iterations took {t*1000:.3f}ms")
