"""
Empirical benchmark for Shortest Cycle in an Undirected Graph BFS
"""
import time
from algorithms.practice.shortest_paths.shortest_cycle_graph import solve_shortest_cycle_graph

def benchmark_shortest_cycle_graph():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_cycle_graph([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_cycle_graph()
    print(f"Shortest Cycle in an Undirected Graph BFS 100 iterations took {t*1000:.3f}ms")
