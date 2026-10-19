"""
Empirical benchmark for Merge Triplets to Form Target Triplet
"""
import time
from algorithms.practice.greedy_algorithms.merge_triplets_target import solve_merge_triplets_target

def benchmark_merge_triplets_target():
    start = time.perf_counter()
    for _ in range(100):
        solve_merge_triplets_target([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_merge_triplets_target()
    print(f"Merge Triplets to Form Target Triplet 100 iterations took {t*1000:.3f}ms")
