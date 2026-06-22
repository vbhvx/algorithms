"""
Empirical benchmark for Trie Autocomplete Frequency Priority Heap
"""
import time
from algorithms.practice.tries_and_prefix.trie_autocomplete import solve_trie_autocomplete

def benchmark_trie_autocomplete():
    start = time.perf_counter()
    for _ in range(100):
        solve_trie_autocomplete([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trie_autocomplete()
    print(f"Trie Autocomplete Frequency Priority Heap 100 iterations took {t*1000:.3f}ms")
