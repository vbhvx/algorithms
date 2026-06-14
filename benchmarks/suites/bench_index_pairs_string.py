"""
Empirical benchmark for Index Pairs of a String Trie Traversal
"""
import time
from algorithms.practice.tries_and_prefix.index_pairs_string import solve_index_pairs_string

def benchmark_index_pairs_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_index_pairs_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_index_pairs_string()
    print(f"Index Pairs of a String Trie Traversal 100 iterations took {t*1000:.3f}ms")
