"""
Empirical benchmark for Swapping Nodes in Linked List Kth from Ends
"""
import time
from algorithms.practice.linked_lists.swapping_nodes_kth import solve_swapping_nodes_kth

def benchmark_swapping_nodes_kth():
    start = time.perf_counter()
    for _ in range(100):
        solve_swapping_nodes_kth([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_swapping_nodes_kth()
    print(f"Swapping Nodes in Linked List Kth from Ends 100 iterations took {t*1000:.3f}ms")
