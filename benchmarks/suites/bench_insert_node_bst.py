"""
Empirical benchmark for Insert into a Binary Search Tree
"""
import time
from algorithms.practice.trees_and_bst.insert_node_bst import solve_insert_node_bst

def benchmark_insert_node_bst():
    start = time.perf_counter()
    for _ in range(100):
        solve_insert_node_bst([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_insert_node_bst()
    print(f"Insert into a Binary Search Tree 100 iterations took {t*1000:.3f}ms")
