"""
Empirical benchmark for Burst Trie Dynamic Container Optimization
"""
import time
from algorithms.practice.tries_and_prefix.burst_trie_dynamic import solve_burst_trie_dynamic

def benchmark_burst_trie_dynamic():
    start = time.perf_counter()
    for _ in range(100):
        solve_burst_trie_dynamic([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_burst_trie_dynamic()
    print(f"Burst Trie Dynamic Container Optimization 100 iterations took {t*1000:.3f}ms")
