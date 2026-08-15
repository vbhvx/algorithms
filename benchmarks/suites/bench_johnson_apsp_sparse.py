"""
Empirical benchmark for Johnson Algorithm APSP Reweighting Dijkstra
"""
import time
from algorithms.practice.shortest_paths.johnson_apsp_sparse import solve_johnson_apsp_sparse

def benchmark_johnson_apsp_sparse():
    start = time.perf_counter()
    for _ in range(100):
        solve_johnson_apsp_sparse([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_johnson_apsp_sparse()
    print(f"Johnson Algorithm APSP Reweighting Dijkstra 100 iterations took {t*1000:.3f}ms")
