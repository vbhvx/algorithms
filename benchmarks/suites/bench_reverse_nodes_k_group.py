"""
Empirical benchmark for Reverse Nodes in K-Group Iterative
"""
import time
from algorithms.practice.linked_lists.reverse_nodes_k_group import solve_reverse_nodes_k_group

def benchmark_reverse_nodes_k_group():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_nodes_k_group([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_nodes_k_group()
    print(f"Reverse Nodes in K-Group Iterative 100 iterations took {t*1000:.3f}ms")
