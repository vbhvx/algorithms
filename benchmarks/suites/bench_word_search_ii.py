"""
Empirical benchmark for Word Search II Trie Backtracking Matrix
"""
import time
from algorithms.practice.tries_and_prefix.word_search_ii import solve_word_search_ii

def benchmark_word_search_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_search_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_search_ii()
    print(f"Word Search II Trie Backtracking Matrix 100 iterations took {t*1000:.3f}ms")
