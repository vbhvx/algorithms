"""
Empirical benchmark for Second Minimum Time to Reach Destination BFS
"""
import time
from algorithms.practice.shortest_paths.second_min_time_reach import solve_second_min_time_reach

def benchmark_second_min_time_reach():
    start = time.perf_counter()
    for _ in range(100):
        solve_second_min_time_reach([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_second_min_time_reach()
    print(f"Second Minimum Time to Reach Destination BFS 100 iterations took {t*1000:.3f}ms")
