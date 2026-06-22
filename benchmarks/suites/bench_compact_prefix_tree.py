"""
Empirical benchmark for Compact Prefix Tree Memory Optimization
"""
import time
from algorithms.practice.tries_and_prefix.compact_prefix_tree import solve_compact_prefix_tree

def benchmark_compact_prefix_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_compact_prefix_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_compact_prefix_tree()
    print(f"Compact Prefix Tree Memory Optimization 100 iterations took {t*1000:.3f}ms")
