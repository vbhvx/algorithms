"""
Empirical benchmark for Number of Connected Components DSU
"""
import time
from algorithms.practice.graphs_and_traversals.num_connected_comp import solve_num_connected_comp

def benchmark_num_connected_comp():
    start = time.perf_counter()
    for _ in range(100):
        solve_num_connected_comp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_num_connected_comp()
    print(f"Number of Connected Components DSU 100 iterations took {t*1000:.3f}ms")
