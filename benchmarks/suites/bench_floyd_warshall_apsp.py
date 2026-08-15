"""
Empirical benchmark for Floyd Warshall All Pairs Dynamic Programming
"""
import time
from algorithms.practice.shortest_paths.floyd_warshall_apsp import solve_floyd_warshall_apsp

def benchmark_floyd_warshall_apsp():
    start = time.perf_counter()
    for _ in range(100):
        solve_floyd_warshall_apsp([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_floyd_warshall_apsp()
    print(f"Floyd Warshall All Pairs Dynamic Programming 100 iterations took {t*1000:.3f}ms")
