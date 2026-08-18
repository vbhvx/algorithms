"""
Empirical benchmark for Reconstruct Itinerary Hierholzer Eulerian Circuit
"""
import time
from algorithms.practice.shortest_paths.hierholzer_eulerian import solve_hierholzer_eulerian

def benchmark_hierholzer_eulerian():
    start = time.perf_counter()
    for _ in range(100):
        solve_hierholzer_eulerian([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_hierholzer_eulerian()
    print(f"Reconstruct Itinerary Hierholzer Eulerian Circuit 100 iterations took {t*1000:.3f}ms")
