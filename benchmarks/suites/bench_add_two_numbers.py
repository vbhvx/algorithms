"""
Empirical benchmark for Add Two Numbers Digit Carry Traversal
"""
import time
from algorithms.practice.linked_lists.add_two_numbers import solve_add_two_numbers

def benchmark_add_two_numbers():
    start = time.perf_counter()
    for _ in range(100):
        solve_add_two_numbers([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_add_two_numbers()
    print(f"Add Two Numbers Digit Carry Traversal 100 iterations took {t*1000:.3f}ms")
