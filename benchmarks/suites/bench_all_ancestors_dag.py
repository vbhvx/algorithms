"""
Empirical benchmark for All Ancestors of a Node in DAG Reverse BFS
"""
import time
from algorithms.practice.shortest_paths.all_ancestors_dag import solve_all_ancestors_dag

def benchmark_all_ancestors_dag():
    start = time.perf_counter()
    for _ in range(100):
        solve_all_ancestors_dag([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_all_ancestors_dag()
    print(f"All Ancestors of a Node in DAG Reverse BFS 100 iterations took {t*1000:.3f}ms")
