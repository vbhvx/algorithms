"""
Empirical benchmark for Euclidean MST via Delaunay Triangulation
"""
import time
from algorithms.practice.minimum_spanning_trees.euclidean_mst_delaunay import solve_euclidean_mst_delaunay

def benchmark_euclidean_mst_delaunay():
    start = time.perf_counter()
    for _ in range(100):
        solve_euclidean_mst_delaunay([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_euclidean_mst_delaunay()
    print(f"Euclidean MST via Delaunay Triangulation 100 iterations took {t*1000:.3f}ms")
