"""
Empirical benchmark for Remove Element In Place Filter
"""
import time
from algorithms.practice.two_pointers.remove_element import solve_remove_element

def benchmark_remove_element():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_element([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_element()
    print(f"Remove Element In Place Filter 100 iterations took {t*1000:.3f}ms")
