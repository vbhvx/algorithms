"""
Empirical benchmark for Snakes and Ladders Board BFS
"""
import time
from algorithms.practice.graphs_and_traversals.snakes_and_ladders import solve_snakes_and_ladders

def benchmark_snakes_and_ladders():
    start = time.perf_counter()
    for _ in range(100):
        solve_snakes_and_ladders([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_snakes_and_ladders()
    print(f"Snakes and Ladders Board BFS 100 iterations took {t*1000:.3f}ms")
