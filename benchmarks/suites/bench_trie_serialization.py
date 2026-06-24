"""
Empirical benchmark for Trie Serialization to Compact Byte Array
"""
import time
from algorithms.practice.tries_and_prefix.trie_serialization import solve_trie_serialization

def benchmark_trie_serialization():
    start = time.perf_counter()
    for _ in range(100):
        solve_trie_serialization([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_trie_serialization()
    print(f"Trie Serialization to Compact Byte Array 100 iterations took {t*1000:.3f}ms")
