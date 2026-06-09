"""
Empirical benchmark for Design Add and Search Words Data Structure Regex
"""
import time
from algorithms.practice.tries_and_prefix.add_search_words import solve_add_search_words

def benchmark_add_search_words():
    start = time.perf_counter()
    for _ in range(100):
        solve_add_search_words([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_add_search_words()
    print(f"Design Add and Search Words Data Structure Regex 100 iterations took {t*1000:.3f}ms")
