"""
Empirical benchmark for Alien Dictionary Topological Sort Shortest Path
"""
import time
from algorithms.practice.shortest_paths.alien_dict_topo import solve_alien_dict_topo

def benchmark_alien_dict_topo():
    start = time.perf_counter()
    for _ in range(100):
        solve_alien_dict_topo([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_alien_dict_topo()
    print(f"Alien Dictionary Topological Sort Shortest Path 100 iterations took {t*1000:.3f}ms")
