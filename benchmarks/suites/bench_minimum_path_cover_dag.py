"""
Empirical benchmark for Minimum Path Cover in Directed Acyclic Graph
"""
import time
from algorithms.practice.network_flow_matching.minimum_path_cover_dag import solve_minimum_path_cover_dag

def benchmark_minimum_path_cover_dag():
    start = time.perf_counter()
    for _ in range(100):
        solve_minimum_path_cover_dag([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_minimum_path_cover_dag()
    print(f"Minimum Path Cover in Directed Acyclic Graph 100 iterations took {t*1000:.3f}ms")
