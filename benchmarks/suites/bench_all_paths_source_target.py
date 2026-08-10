"""
Empirical benchmark for All Paths From Source to Target DAG DFS
"""
import time
from algorithms.practice.graphs_and_traversals.all_paths_source_target import solve_all_paths_source_target

def benchmark_all_paths_source_target():
    start = time.perf_counter()
    for _ in range(100):
        solve_all_paths_source_target([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_all_paths_source_target()
    print(f"All Paths From Source to Target DAG DFS 100 iterations took {t*1000:.3f}ms")
