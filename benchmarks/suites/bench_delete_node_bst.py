"""
Empirical benchmark for Delete Node in BST Inorder Successor
"""
import time
from algorithms.practice.trees_and_bst.delete_node_bst import solve_delete_node_bst

def benchmark_delete_node_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_delete_node_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_delete_node_bst()
    print(f"Delete Node in BST Inorder Successor 100 iterations took {t*1000:.3f}ms")
