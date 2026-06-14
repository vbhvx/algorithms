"""
Empirical benchmark for Palindrome Pairs Trie Word Reversal
"""
import time
from algorithms.practice.tries_and_prefix.palindrome_pairs import solve_palindrome_pairs

def benchmark_palindrome_pairs():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindrome_pairs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindrome_pairs()
    print(f"Palindrome Pairs Trie Word Reversal 100 iterations took {t*1000:.3f}ms")
