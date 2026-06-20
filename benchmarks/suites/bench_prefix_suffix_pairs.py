"""
Empirical benchmark for Count Prefix and Suffix Pairs Trie Double Hash
"""
import time
from algorithms.practice.tries_and_prefix.prefix_suffix_pairs import solve_prefix_suffix_pairs

def benchmark_prefix_suffix_pairs():
    start = time.perf_counter()
    for _ in range(100):
        solve_prefix_suffix_pairs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_prefix_suffix_pairs()
    print(f"Count Prefix and Suffix Pairs Trie Double Hash 100 iterations took {t*1000:.3f}ms")
