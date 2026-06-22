"""
Empirical benchmark for Ternary Search Tree Three-Way Branching
"""
import time
from algorithms.practice.tries_and_prefix.ternary_search_tree import solve_ternary_search_tree

def benchmark_ternary_search_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_ternary_search_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ternary_search_tree()
    print(f"Ternary Search Tree Three-Way Branching 100 iterations took {t*1000:.3f}ms")
