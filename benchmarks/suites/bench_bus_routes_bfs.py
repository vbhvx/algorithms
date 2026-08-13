"""
Empirical benchmark for Bus Routes Breadth-First Route Graph
"""
import time
from algorithms.practice.graphs_and_traversals.bus_routes_bfs import solve_bus_routes_bfs

def benchmark_bus_routes_bfs():
    start = time.perf_counter()
    for _ in range(100):
        solve_bus_routes_bfs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bus_routes_bfs()
    print(f"Bus Routes Breadth-First Route Graph 100 iterations took {t*1000:.3f}ms")
