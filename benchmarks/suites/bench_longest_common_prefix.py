"""
Empirical benchmark for Longest Common Prefix Trie Branch Search
"""
import time
from algorithms.practice.tries_and_prefix.longest_common_prefix import solve_longest_common_prefix

def benchmark_longest_common_prefix():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_common_prefix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_common_prefix()
    print(f"Longest Common Prefix Trie Branch Search 100 iterations took {t*1000:.3f}ms")
