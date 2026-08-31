"""
Empirical benchmark for Edmonds-Karp Max Flow BFS Residual Graph
"""
import time
from algorithms.practice.network_flow_matching.edmonds_karp_maxflow import solve_edmonds_karp_maxflow

def benchmark_edmonds_karp_maxflow():
    start = time.perf_counter()
    for _ in range(100):
        solve_edmonds_karp_maxflow([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_edmonds_karp_maxflow()
    print(f"Edmonds-Karp Max Flow BFS Residual Graph 100 iterations took {t*1000:.3f}ms")
