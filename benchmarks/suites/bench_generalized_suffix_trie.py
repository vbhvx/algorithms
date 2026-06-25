"""
Empirical benchmark for Generalized Suffix Trie Multi-String Match
"""
import time
from algorithms.practice.tries_and_prefix.generalized_suffix_trie import solve_generalized_suffix_trie

def benchmark_generalized_suffix_trie():
    start = time.perf_counter()
    for _ in range(100):
        solve_generalized_suffix_trie([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_generalized_suffix_trie()
    print(f"Generalized Suffix Trie Multi-String Match 100 iterations took {t*1000:.3f}ms")
