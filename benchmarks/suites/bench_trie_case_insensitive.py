"""
Empirical benchmark for Case Insensitive Trie Canonical Index
"""
import time
from algorithms.practice.tries_and_prefix.trie_case_insensitive import solve_trie_case_insensitive

def benchmark_trie_case_insensitive():
    start = time.perf_counter()
    for _ in range(100):
        solve_trie_case_insensitive([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trie_case_insensitive()
    print(f"Case Insensitive Trie Canonical Index 100 iterations took {t*1000:.3f}ms")
