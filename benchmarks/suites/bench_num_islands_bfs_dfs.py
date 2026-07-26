"""
Empirical benchmark for Number of Islands Grid Flood Fill
"""
import time
from algorithms.practice.graphs_and_traversals.num_islands_bfs_dfs import solve_num_islands_bfs_dfs

def benchmark_num_islands_bfs_dfs():
    start = time.perf_counter()
    for _ in range(100):
        solve_num_islands_bfs_dfs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_num_islands_bfs_dfs()
    print(f"Number of Islands Grid Flood Fill 100 iterations took {t*1000:.3f}ms")
