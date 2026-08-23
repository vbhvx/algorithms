"""
Empirical benchmark for Connecting Cities With Minimum Cost Kruskal
"""
import time
from algorithms.practice.minimum_spanning_trees.connecting_cities_cost import solve_connecting_cities_cost

def benchmark_connecting_cities_cost():
    start = time.perf_counter()
    for _ in range(100):
        solve_connecting_cities_cost([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_connecting_cities_cost()
    print(f"Connecting Cities With Minimum Cost Kruskal 100 iterations took {t*1000:.3f}ms")
