"""
Empirical benchmark for Walls and Gates Multi-Source Distance BFS
"""
import time
from algorithms.practice.graphs_and_traversals.walls_and_gates import solve_walls_and_gates

def benchmark_walls_and_gates():
    start = time.perf_counter()
    for _ in range(100):
        solve_walls_and_gates([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_walls_and_gates()
    print(f"Walls and Gates Multi-Source Distance BFS 100 iterations took {t*1000:.3f}ms")
