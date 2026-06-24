"""
Empirical benchmark for Aho Corasick Trie Dictionary Matching
"""
import time
from algorithms.practice.tries_and_prefix.aho_corasick_trie import solve_aho_corasick_trie

def benchmark_aho_corasick_trie():
    start = time.perf_counter()
    for _ in range(100):
        solve_aho_corasick_trie([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_aho_corasick_trie()
    print(f"Aho Corasick Trie Dictionary Matching 100 iterations took {t*1000:.3f}ms")
