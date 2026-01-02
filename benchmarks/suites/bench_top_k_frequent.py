"""
Empirical benchmark for Top K Frequent Elements Bucket Sort
"""
import time
from algorithms.practice.arrays_and_hashing.top_k_frequent import solve_top_k_frequent

def benchmark_top_k_frequent():
    start = time.perf_counter()
    for _ in range(100):
        solve_top_k_frequent([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_top_k_frequent()
    print(f"Top K Frequent Elements Bucket Sort 100 iterations took {t*1000:.3f}ms")
