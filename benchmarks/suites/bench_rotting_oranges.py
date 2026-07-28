"""
Empirical benchmark for Rotting Oranges Multi-Source BFS Queue
"""
import time
from algorithms.practice.graphs_and_traversals.rotting_oranges import solve_rotting_oranges

def benchmark_rotting_oranges():
    start = time.perf_counter()
    for _ in range(100):
        solve_rotting_oranges([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_rotting_oranges()
    print(f"Rotting Oranges Multi-Source BFS Queue 100 iterations took {t*1000:.3f}ms")
