"""
Empirical benchmark for Lowest Common Ancestor BST Value Property
"""
import time
from algorithms.practice.trees_and_bst.lca_bst import solve_lca_bst

def benchmark_lca_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_lca_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_lca_bst()
    print(f"Lowest Common Ancestor BST Value Property 100 iterations took {t*1000:.3f}ms")
