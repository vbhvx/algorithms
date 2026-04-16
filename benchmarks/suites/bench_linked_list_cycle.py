"""
Empirical benchmark for Linked List Cycle Floyd Tortoise Hare
"""
import time
from algorithms.practice.linked_lists.linked_list_cycle import solve_linked_list_cycle

def benchmark_linked_list_cycle():
    start = time.perf_counter()
    for _ in range(100):
        solve_linked_list_cycle([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_linked_list_cycle()
    print(f"Linked List Cycle Floyd Tortoise Hare 100 iterations took {t*1000:.3f}ms")
