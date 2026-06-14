"""
Empirical benchmark for Multi Search Trie Suffix Matching
"""
import time
from algorithms.practice.tries_and_prefix.multi_search_trie import solve_multi_search_trie

def benchmark_multi_search_trie():
    start = time.perf_counter()
    for _ in range(100):
        solve_multi_search_trie([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_multi_search_trie()
    print(f"Multi Search Trie Suffix Matching 100 iterations took {t*1000:.3f}ms")
