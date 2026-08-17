"""
Empirical benchmark for Modify Graph Edge Weights Dijkstra Difference
"""
import time
from algorithms.practice.shortest_paths.modify_graph_weights import solve_modify_graph_weights

def benchmark_modify_graph_weights():
    start = time.perf_counter()
    for _ in range(100):
        solve_modify_graph_weights([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_modify_graph_weights()
    print(f"Modify Graph Edge Weights Dijkstra Difference 100 iterations took {t*1000:.3f}ms")
