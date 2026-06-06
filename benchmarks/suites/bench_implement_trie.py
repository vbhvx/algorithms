"""
Empirical benchmark for Implement Trie Prefix Tree Insert Search StartsWith
"""
import time
from algorithms.practice.tries_and_prefix.implement_trie import solve_implement_trie

def benchmark_implement_trie():
    start = time.perf_counter()
    for _ in range(100):
        solve_implement_trie([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_implement_trie()
    print(f"Implement Trie Prefix Tree Insert Search StartsWith 100 iterations took {t*1000:.3f}ms")
