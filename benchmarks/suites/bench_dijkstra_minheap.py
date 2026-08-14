"""
Empirical benchmark for Dijkstra Shortest Path Adjacency MinHeap
"""
import time
from algorithms.practice.shortest_paths.dijkstra_minheap import solve_dijkstra_minheap

def benchmark_dijkstra_minheap():
    start = time.perf_counter()
    for _ in range(100):
        solve_dijkstra_minheap([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dijkstra_minheap()
    print(f"Dijkstra Shortest Path Adjacency MinHeap 100 iterations took {t*1000:.3f}ms")
