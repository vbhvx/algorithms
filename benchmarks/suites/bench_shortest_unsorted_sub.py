"""
Empirical benchmark for Shortest Unsorted Subarray
"""
import time
from algorithms.practice.two_pointers.shortest_unsorted_sub import solve_shortest_unsorted_sub

def benchmark_shortest_unsorted_sub():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_unsorted_sub([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_unsorted_sub()
    print(f"Shortest Unsorted Subarray 100 iterations took {t*1000:.3f}ms")
