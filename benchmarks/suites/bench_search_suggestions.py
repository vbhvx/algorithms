"""
Empirical benchmark for Search Suggestions System Lexicographical Trie
"""
import time
from algorithms.practice.tries_and_prefix.search_suggestions import solve_search_suggestions

def benchmark_search_suggestions():
    start = time.perf_counter()
    for _ in range(100):
        solve_search_suggestions([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_search_suggestions()
    print(f"Search Suggestions System Lexicographical Trie 100 iterations took {t*1000:.3f}ms")
