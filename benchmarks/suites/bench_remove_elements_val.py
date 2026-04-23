"""
Empirical benchmark for Remove Linked List Elements by Value
"""
import time
from algorithms.practice.linked_lists.remove_elements_val import solve_remove_elements_val

def benchmark_remove_elements_val():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_elements_val([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_elements_val()
    print(f"Remove Linked List Elements by Value 100 iterations took {t*1000:.3f}ms")
