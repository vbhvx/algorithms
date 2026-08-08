"""
Empirical benchmark for Find Eventual Safe States Cycle Detection
"""
import time
from algorithms.practice.graphs_and_traversals.find_eventual_safe import solve_find_eventual_safe

def benchmark_find_eventual_safe():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_eventual_safe([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_eventual_safe()
    print(f"Find Eventual Safe States Cycle Detection 100 iterations took {t*1000:.3f}ms")
