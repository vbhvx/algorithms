"""
Empirical benchmark for Shortest Bridge Two Islands BFS Expansion
"""
import time
from algorithms.practice.graphs_and_traversals.shortest_bridge_island import solve_shortest_bridge_island

def benchmark_shortest_bridge_island():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_bridge_island([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_bridge_island()
    print(f"Shortest Bridge Two Islands BFS Expansion 100 iterations took {t*1000:.3f}ms")
