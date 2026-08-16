"""
Empirical benchmark for Minimum Cost to Make at Least One Valid Path 0-1 BFS
"""
import time
from algorithms.practice.shortest_paths.min_cost_valid_path import solve_min_cost_valid_path

def benchmark_min_cost_valid_path():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_valid_path([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_valid_path()
    print(f"Minimum Cost to Make at Least One Valid Path 0-1 BFS 100 iterations took {t*1000:.3f}ms")
