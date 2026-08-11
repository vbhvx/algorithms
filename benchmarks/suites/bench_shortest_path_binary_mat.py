"""
Empirical benchmark for Shortest Path in Binary Matrix 8-Way BFS
"""
import time
from algorithms.practice.graphs_and_traversals.shortest_path_binary_mat import solve_shortest_path_binary_mat

def benchmark_shortest_path_binary_mat():
    start = time.perf_counter()
    for _ in range(100):
        solve_shortest_path_binary_mat([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_shortest_path_binary_mat()
    print(f"Shortest Path in Binary Matrix 8-Way BFS 100 iterations took {t*1000:.3f}ms")
