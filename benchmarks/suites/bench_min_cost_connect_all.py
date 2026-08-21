"""
Empirical benchmark for Min Cost to Connect All Points Manhattan MST
"""
import time
from algorithms.practice.minimum_spanning_trees.min_cost_connect_all import solve_min_cost_connect_all

def benchmark_min_cost_connect_all():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cost_connect_all([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cost_connect_all()
    print(f"Min Cost to Connect All Points Manhattan MST 100 iterations took {t*1000:.3f}ms")
