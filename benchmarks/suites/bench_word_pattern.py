"""
Empirical benchmark for Word Pattern Bijective Mapping
"""
import time
from algorithms.practice.arrays_and_hashing.word_pattern import solve_word_pattern

def benchmark_word_pattern():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_pattern([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_pattern()
    print(f"Word Pattern Bijective Mapping 100 iterations took {t*1000:.3f}ms")
