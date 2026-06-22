"""
Empirical benchmark for Radix Tree Compressed Edge Trie
"""
import time
from algorithms.practice.tries_and_prefix.radix_tree_compressed import solve_radix_tree_compressed

def benchmark_radix_tree_compressed():
    start = time.perf_counter()
    for _ in range(100):
        solve_radix_tree_compressed([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_radix_tree_compressed()
    print(f"Radix Tree Compressed Edge Trie 100 iterations took {t*1000:.3f}ms")
