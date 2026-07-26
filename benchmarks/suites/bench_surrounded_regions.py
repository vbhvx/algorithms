"""
Empirical benchmark for Surrounded Regions Boundary Flood Fill
"""
import time
from algorithms.practice.graphs_and_traversals.surrounded_regions import solve_surrounded_regions

def benchmark_surrounded_regions():
    start = time.perf_counter()
    for _ in range(100):
        solve_surrounded_regions([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_surrounded_regions()
    print(f"Surrounded Regions Boundary Flood Fill 100 iterations took {t*1000:.3f}ms")
