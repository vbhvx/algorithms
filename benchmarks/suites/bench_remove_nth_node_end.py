"""
Empirical benchmark for Remove Nth Node From End Fast Slow
"""
import time
from algorithms.practice.linked_lists.remove_nth_node_end import solve_remove_nth_node_end

def benchmark_remove_nth_node_end():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_nth_node_end([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_nth_node_end()
    print(f"Remove Nth Node From End Fast Slow 100 iterations took {t*1000:.3f}ms")
