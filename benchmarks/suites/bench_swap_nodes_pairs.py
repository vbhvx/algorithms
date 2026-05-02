"""
Empirical benchmark for Swap Nodes in Pairs Iterative Pointer Swaps
"""
import time
from algorithms.practice.linked_lists.swap_nodes_pairs import solve_swap_nodes_pairs

def benchmark_swap_nodes_pairs():
    start = time.perf_counter()
    for _ in range(100):
        solve_swap_nodes_pairs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_swap_nodes_pairs()
    print(f"Swap Nodes in Pairs Iterative Pointer Swaps 100 iterations took {t*1000:.3f}ms")
