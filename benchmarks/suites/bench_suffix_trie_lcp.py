"""
Empirical benchmark for Suffix Trie for Longest Common Substring
"""
import time
from algorithms.practice.tries_and_prefix.suffix_trie_lcp import solve_suffix_trie_lcp

def benchmark_suffix_trie_lcp():
    start = time.perf_counter()
    for _ in range(100):
        solve_suffix_trie_lcp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_suffix_trie_lcp()
    print(f"Suffix Trie for Longest Common Substring 100 iterations took {t*1000:.3f}ms")
