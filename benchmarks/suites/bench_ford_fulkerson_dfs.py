"""
Empirical benchmark for Ford-Fulkerson Max Flow Augmenting Paths
"""
import time
from algorithms.practice.network_flow_matching.ford_fulkerson_dfs import solve_ford_fulkerson_dfs

def benchmark_ford_fulkerson_dfs():
    start = time.perf_counter()
    for _ in range(100):
        solve_ford_fulkerson_dfs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ford_fulkerson_dfs()
    print(f"Ford-Fulkerson Max Flow Augmenting Paths 100 iterations took {t*1000:.3f}ms")
