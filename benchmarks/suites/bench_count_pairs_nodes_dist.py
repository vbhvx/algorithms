"""
Empirical benchmark for Count Pairs of Nodes in Distance Bound
"""
import time
from algorithms.practice.shortest_paths.count_pairs_nodes_dist import solve_count_pairs_nodes_dist

def benchmark_count_pairs_nodes_dist():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_pairs_nodes_dist([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_pairs_nodes_dist()
    print(f"Count Pairs of Nodes in Distance Bound 100 iterations took {t*1000:.3f}ms")
