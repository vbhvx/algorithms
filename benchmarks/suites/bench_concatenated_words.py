"""
Empirical benchmark for Concatenated Words Trie Memoized DFS
"""
import time
from algorithms.practice.tries_and_prefix.concatenated_words import solve_concatenated_words

def benchmark_concatenated_words():
    start = time.perf_counter()
    for _ in range(100):
        solve_concatenated_words([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_concatenated_words()
    print(f"Concatenated Words Trie Memoized DFS 100 iterations took {t*1000:.3f}ms")
