"""
Empirical benchmark for Find the City with Smallest Number of Neighbors
"""
import time
from algorithms.practice.shortest_paths.find_city_neighbors import solve_find_city_neighbors

def benchmark_find_city_neighbors():
    start = time.perf_counter()
    for _ in range(100):
        solve_find_city_neighbors([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_find_city_neighbors()
    print(f"Find the City with Smallest Number of Neighbors 100 iterations took {t*1000:.3f}ms")
