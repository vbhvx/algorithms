"""
Empirical benchmark for Delete the Middle Node of Linked List
"""
import time
from algorithms.practice.linked_lists.delete_middle_node import solve_delete_middle_node

def benchmark_delete_middle_node():
    start = time.perf_counter()
    for _ in range(100):
        solve_delete_middle_node([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_delete_middle_node()
    print(f"Delete the Middle Node of Linked List 100 iterations took {t*1000:.3f}ms")
