"""
Empirical benchmark for Bitwise Trie for Maximum Subset XOR Basis
"""
import time
from algorithms.practice.tries_and_prefix.bitwise_trie_xor import solve_bitwise_trie_xor

def benchmark_bitwise_trie_xor():
    start = time.perf_counter()
    for _ in range(100):
        solve_bitwise_trie_xor([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bitwise_trie_xor()
    print(f"Bitwise Trie for Maximum Subset XOR Basis 100 iterations took {t*1000:.3f}ms")
