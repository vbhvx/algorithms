"""
Empirical benchmark for Reachable Nodes in Subdivided Graph Dijkstra
"""
import time
from algorithms.practice.shortest_paths.reachable_nodes_subdiv import solve_reachable_nodes_subdiv

def benchmark_reachable_nodes_subdiv():
    start = time.perf_counter()
    for _ in range(100):
        solve_reachable_nodes_subdiv([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reachable_nodes_subdiv()
    print(f"Reachable Nodes in Subdivided Graph Dijkstra 100 iterations took {t*1000:.3f}ms")
