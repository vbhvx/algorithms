"""
Empirical benchmark for All Nodes Distance K in Binary Tree Graph
"""
import time
from algorithms.practice.trees_and_bst.all_nodes_k_dist import solve_all_nodes_k_dist

def benchmark_all_nodes_k_dist():
    start = time.perf_counter()
    for _ in range(100):
        solve_all_nodes_k_dist([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_all_nodes_k_dist()
    print(f"All Nodes Distance K in Binary Tree Graph 100 iterations took {t*1000:.3f}ms")
