"""
Empirical benchmark for Trie Wildcard Pattern Matching Backtrack
"""
import time
from algorithms.practice.tries_and_prefix.trie_wildcard_search import solve_trie_wildcard_search

def benchmark_trie_wildcard_search():
    start = time.perf_counter()
    for _ in range(100):
        solve_trie_wildcard_search([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trie_wildcard_search()
    print(f"Trie Wildcard Pattern Matching Backtrack 100 iterations took {t*1000:.3f}ms")
