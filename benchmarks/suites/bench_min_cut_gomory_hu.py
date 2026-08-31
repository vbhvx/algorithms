"""
Empirical benchmark for Gomory-Hu Tree Minimum Cut All Pairs
"""
import time
from algorithms.practice.minimum_spanning_trees.min_cut_gomory_hu import solve_min_cut_gomory_hu

def benchmark_min_cut_gomory_hu():
    start = time.perf_counter()
    for _ in range(100):
        solve_min_cut_gomory_hu([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_min_cut_gomory_hu()
    print(f"Gomory-Hu Tree Minimum Cut All Pairs 100 iterations took {t*1000:.3f}ms")
