"""
Empirical benchmark for Open the Lock 4-Dial BFS Shortest Path
"""
import time
from algorithms.practice.graphs_and_traversals.open_the_lock import solve_open_the_lock

def benchmark_open_the_lock():
    start = time.perf_counter()
    for _ in range(100):
        solve_open_the_lock([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_open_the_lock()
    print(f"Open the Lock 4-Dial BFS Shortest Path 100 iterations took {t*1000:.3f}ms")
