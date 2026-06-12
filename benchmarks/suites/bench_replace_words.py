"""
Empirical benchmark for Replace Words Trie Shortest Root Match
"""
import time
from algorithms.practice.tries_and_prefix.replace_words import solve_replace_words

def benchmark_replace_words():
    start = time.perf_counter()
    for _ in range(100):
        solve_replace_words([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_replace_words()
    print(f"Replace Words Trie Shortest Root Match 100 iterations took {t*1000:.3f}ms")
