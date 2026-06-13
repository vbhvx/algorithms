"""
Empirical benchmark for Map Sum Pairs Trie Prefix Score Accumulator
"""
import time
from algorithms.practice.tries_and_prefix.map_sum_pairs import solve_map_sum_pairs

def benchmark_map_sum_pairs():
    start = time.perf_counter()
    for _ in range(100):
        solve_map_sum_pairs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_map_sum_pairs()
    print(f"Map Sum Pairs Trie Prefix Score Accumulator 100 iterations took {t*1000:.3f}ms")
