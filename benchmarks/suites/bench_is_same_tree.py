"""
Empirical benchmark for Same Tree Structural Equivalence
"""
import time
from algorithms.practice.trees_and_bst.is_same_tree import solve_is_same_tree

def benchmark_is_same_tree():
    start = time.perf_counter()
    for _ in range(100):
        solve_is_same_tree([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_is_same_tree()
    print(f"Same Tree Structural Equivalence 100 iterations took {t*1000:.3f}ms")
