"""
Empirical benchmark for Design Graph With Shortest Path Calculator
"""
import time
from algorithms.practice.shortest_paths.design_graph_dijkstra import solve_design_graph_dijkstra

def benchmark_design_graph_dijkstra():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_graph_dijkstra([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_graph_dijkstra()
    print(f"Design Graph With Shortest Path Calculator 100 iterations took {t*1000:.3f}ms")
