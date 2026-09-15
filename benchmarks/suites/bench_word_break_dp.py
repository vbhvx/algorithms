"""
Empirical benchmark for Word Break Prefix Verification Set
"""
import time
from algorithms.practice.dynamic_programming_1d.word_break_dp import solve_word_break_dp

def benchmark_word_break_dp():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_break_dp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_break_dp()
    print(f"Word Break Prefix Verification Set 100 iterations took {t*1000:.3f}ms")
