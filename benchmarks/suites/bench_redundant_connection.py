"""
Empirical benchmark for Redundant Connection Disjoint Set Union
"""
import time
from algorithms.practice.graphs_and_traversals.redundant_connection import solve_redundant_connection

def benchmark_redundant_connection():
    start = time.perf_counter()
    for _ in range(100):
        solve_redundant_connection([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_redundant_connection()
    print(f"Redundant Connection Disjoint Set Union 100 iterations took {t*1000:.3f}ms")
