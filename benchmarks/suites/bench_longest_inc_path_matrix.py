"""
Empirical benchmark for Longest Increasing Path in Matrix DFS Memo
"""
import time
from algorithms.practice.dynamic_programming_2d.longest_inc_path_matrix import solve_longest_inc_path_matrix

def benchmark_longest_inc_path_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_longest_inc_path_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_longest_inc_path_matrix()
    print(f"Longest Increasing Path in Matrix DFS Memo 100 iterations took {t*1000:.3f}ms")
