"""
Empirical benchmark for Delete Node in Linked List Without Head
"""
import time
from algorithms.practice.linked_lists.delete_node_in_list import solve_delete_node_in_list

def benchmark_delete_node_in_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_delete_node_in_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_delete_node_in_list()
    print(f"Delete Node in Linked List Without Head 100 iterations took {t*1000:.3f}ms")
