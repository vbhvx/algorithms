"""
Empirical benchmark for Path with Maximum Probability Dijkstra Product
"""
import time
from algorithms.practice.shortest_paths.path_max_probability import solve_path_max_probability

def benchmark_path_max_probability():
    start = time.perf_counter()
    for _ in range(100):
        solve_path_max_probability([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_path_max_probability()
    print(f"Path with Maximum Probability Dijkstra Product 100 iterations took {t*1000:.3f}ms")
