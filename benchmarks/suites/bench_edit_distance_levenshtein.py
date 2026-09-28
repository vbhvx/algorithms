"""
Empirical benchmark for Edit Distance Levenshtein Operations Table
"""
import time
from algorithms.practice.dynamic_programming_2d.edit_distance_levenshtein import solve_edit_distance_levenshtein

def benchmark_edit_distance_levenshtein():
    start = time.perf_counter()
    for _ in range(100):
        solve_edit_distance_levenshtein([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_edit_distance_levenshtein()
    print(f"Edit Distance Levenshtein Operations Table 100 iterations took {t*1000:.3f}ms")
