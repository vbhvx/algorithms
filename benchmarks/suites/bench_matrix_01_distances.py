"""
Empirical benchmark for 01 Matrix Multi-Source BFS Distance Field
"""
import time
from algorithms.practice.graphs_and_traversals.matrix_01_distances import solve_matrix_01_distances

def benchmark_matrix_01_distances():
    start = time.perf_counter()
    for _ in range(100):
        solve_matrix_01_distances([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_matrix_01_distances()
    print(f"01 Matrix Multi-Source BFS Distance Field 100 iterations took {t*1000:.3f}ms")
