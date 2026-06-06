"""
Empirical benchmark for Flatten Binary Tree to Linked List Preorder
"""
import time
from algorithms.practice.trees_and_bst.flatten_tree_linked import solve_flatten_tree_linked

def benchmark_flatten_tree_linked():
    start = time.perf_counter()
    for _ in range(100):
        solve_flatten_tree_linked([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_flatten_tree_linked()
    print(f"Flatten Binary Tree to Linked List Preorder 100 iterations took {t*1000:.3f}ms")
