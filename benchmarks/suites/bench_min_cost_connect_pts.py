"""
Empirical benchmark for Min Cost to Connect All Points Prim Kruskal
"""
import time
from algorithms.practice.shortest_paths.min_cost_connect_pts import solve_min_cost_connect_pts

def benchmark_min_cost_connect_pts():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_connect_pts([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_connect_pts()
    print(f"Min Cost to Connect All Points Prim Kruskal 100 iterations took {t*1000:.3f}ms")
