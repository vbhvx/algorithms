"""
Empirical benchmark for Count Negative Numbers in Sorted Matrix
"""
import time
from algorithms.practice.binary_search.count_negatives_matrix import solve_count_negatives_matrix

def benchmark_count_negatives_matrix():
    start = time.perf_counter()
    for _ in range(100):
        solve_count_negatives_matrix([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_count_negatives_matrix()
    print(f"Count Negative Numbers in Sorted Matrix 100 iterations took {t*1000:.3f}ms")
