"""
Empirical benchmark for Keys and Rooms Reachability BFS
"""
import time
from algorithms.practice.graphs_and_traversals.keys_and_rooms import solve_keys_and_rooms

def benchmark_keys_and_rooms():
    start = time.perf_counter()
    for _ in range(100):
        solve_keys_and_rooms([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_keys_and_rooms()
    print(f"Keys and Rooms Reachability BFS 100 iterations took {t*1000:.3f}ms")
