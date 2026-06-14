"""
Empirical benchmark for Prefix and Suffix Search Word Filter Trie
"""
import time
from algorithms.practice.tries_and_prefix.prefix_suffix_search import solve_prefix_suffix_search

def benchmark_prefix_suffix_search():
    start = time.perf_counter()
    for _ in range(100):
        solve_prefix_suffix_search([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_prefix_suffix_search()
    print(f"Prefix and Suffix Search Word Filter Trie 100 iterations took {t*1000:.3f}ms")
