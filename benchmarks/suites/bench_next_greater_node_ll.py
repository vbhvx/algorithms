"""
Empirical benchmark for Next Greater Node in Linked List Monotonic
"""
import time
from algorithms.practice.linked_lists.next_greater_node_ll import solve_next_greater_node_ll

def benchmark_next_greater_node_ll():
    start = time.perf_counter()
    for _ in range(100):
        solve_next_greater_node_ll([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_next_greater_node_ll()
    print(f"Next Greater Node in Linked List Monotonic 100 iterations took {t*1000:.3f}ms")
